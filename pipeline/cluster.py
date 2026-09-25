"""Step 3: group page items into recipes (entity resolution). No API calls.

A page can hold several recipes, so the unit is an item, referenced as "157#2"
(second item on page 157). A bare page label like "157" means its first item.

1. Chain continuation items onto the recipe they continue: the one just before, or the last one
   with the same title when other pages sit in between (page 53 continuing page 51).
2. Merge chains that are copies of one dish: same title and the same ingredients and quantities.
   A shared title alone isn't enough (two different "Pastel navideño"), and matching ingredients
   under different titles only produce a suggestion in cache/review.md.
3. Apply manual fixes from data/overrides.yaml.
"""

import re
import unicodedata
from itertools import combinations

import yaml
from rapidfuzz import fuzz

from .config import CLUSTERS_FILE, DIFFERENT_INGREDIENTS, OVERRIDES_FILE, SAME_INGREDIENTS, TITLE_MATCH_SCORE
from .extract import cache_path
from .pages import list_pages
from .source import Source, shared_ingredients
from .store import read_json, write_json, write_review_section


def normalize(title: str) -> str:
    text = unicodedata.normalize("NFKD", title.lower())
    text = "".join(c for c in text if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", text)).strip()


def ref(value) -> str:
    """Normalize an override entry (157, "157", "157#2") to an item ref."""
    value = str(value)
    return value if "#" in value else f"{value}#1"


def load_overrides() -> dict:
    if not OVERRIDES_FILE.exists():
        return {}
    return yaml.safe_load(OVERRIDES_FILE.read_text(encoding="utf-8")) or {}


def _chain(pages: list[dict], overrides: dict, log: list[str]) -> list[dict]:
    drop = {str(d) for d in overrides.get("drop") or []}
    split = {ref(s) for s in overrides.get("split") or []}
    kinds = {ref(k): v for k, v in (overrides.get("kind") or {}).items()}
    chains: list[dict] = []
    previous_continues = False
    for data in pages:
        label = data["page"]
        if label in drop:
            log.append(f"- página {label}: descartada (overrides)")
            previous_continues = False
            continue
        if not data["items"]:
            log.append(f"- página {label}: sin recetas ({data.get('skip_reason', '') or 'vacía'})")
            continue
        for index, item in enumerate(data["items"]):
            item_ref = f"{label}#{index + 1}"
            if item_ref in drop:
                log.append(f"- {item_ref}: descartado (overrides)")
                continue
            title = normalize(item["normalized_title"] or item["title"])
            kind = kinds.get(item_ref, item["kind"])
            last = chains[-1] if chains else None
            continues = index == 0 and (item.get("is_continuation", False) or (previous_continues and not title))
            same_title = last is not None and (not title or title == last["title"])
            if last and continues and same_title and item_ref not in split:
                last["refs"].append(item_ref)
                last["items"].append(item)
                continue
            if continues and item_ref not in split:
                earlier = next((c for c in reversed(chains) if title and c["title"] == title and c["kind"] == kind), None)
                if earlier:
                    earlier["refs"].append(item_ref)
                    earlier["items"].append(item)
                    log.append(f"- {item_ref}: continúa {earlier['refs'][0]} (con otras páginas en medio)")
                    continue
                log.append(f"- {item_ref}: continuación sin receta previa; queda como fragmento")
            chains.append({"title": title, "display": item["title"], "kind": kind, "refs": [item_ref], "items": [item]})
        previous_continues = data.get("continues_next", False)
    return chains


def _merge(chains: list[dict], overrides: dict, log: list[str]) -> list[list[dict]]:
    parent = list(range(len(chains)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    ref_to_chain = {r: i for i, c in enumerate(chains) for r in c["refs"]}
    apart = {frozenset(ref_to_chain.get(ref(r)) for r in pair) for pair in overrides.get("keep_apart") or []}

    undecided: list[tuple[int, int, str]] = []  # reported unless overrides.yaml merges them anyway
    sources = []
    for chain in chains:
        source = Source()
        for item in chain["items"]:
            source.add(item)
        sources.append(source)

    for i, j in combinations(range(len(chains)), 2):
        a, b = chains[i], chains[j]
        if not a["title"] or not b["title"] or a["kind"] != b["kind"] or frozenset((i, j)) in apart:
            continue
        same_title = fuzz.ratio(a["title"], b["title"]) >= TITLE_MATCH_SCORE
        shared = shared_ingredients(sources[i], sources[j])
        pair = f"{a['refs'][0]} {a['display']!r} / {b['refs'][0]} {b['display']!r}"
        merge_hint = f'si son la misma, añade `- ["{a["refs"][0]}", "{b["refs"][0]}"]` a merge en overrides.yaml'
        if shared is None:
            # Tips and fragments have no ingredient list to compare; the title decides.
            if same_title:
                parent[find(j)] = find(i)
                log.append(f"- unidas: {pair} (mismo título, sin ingredientes que comparar)")
        elif same_title and shared >= SAME_INGREDIENTS:
            parent[find(j)] = find(i)
            log.append(f"- unidas: {pair} (mismo título, {shared:.0%} de ingredientes iguales)")
        elif same_title and shared >= DIFFERENT_INGREDIENTS:
            # Usually one copy written differently (a sauce folded into one line); worth a look.
            parent[find(j)] = find(i)
            log.append(
                f"- ¿bien unidas? {pair}: mismo título, solo {shared:.0%} de ingredientes iguales"
                f' → si son distintas, añade `- ["{a["refs"][0]}", "{b["refs"][0]}"]` a keep_apart en overrides.yaml'
            )
        elif same_title:
            undecided.append((i, j, f"- separadas: {pair}: mismo título pero recetas distintas ({shared:.0%} de ingredientes iguales) → {merge_hint}"))
        elif shared >= SAME_INGREDIENTS:
            undecided.append((i, j, f"- ¿misma receta con otro título? {pair}: {shared:.0%} de ingredientes iguales → {merge_hint}"))

    for group in overrides.get("merge") or []:
        ids = [ref_to_chain[ref(r)] for r in group if ref(r) in ref_to_chain]
        for other in ids[1:]:
            parent[find(other)] = find(ids[0])
    log += [text for i, j, text in undecided if find(i) != find(j)]

    groups: dict[int, list[dict]] = {}
    for i, c in enumerate(chains):
        groups.setdefault(find(i), []).append(c)
    return list(groups.values())


def run() -> None:
    pages, missing = [], []
    for page in list_pages():
        path = cache_path(page)
        if path.exists():
            pages.append(read_json(path))
        else:
            missing.append(page.label)
    if missing:
        print(f"Aviso: {len(missing)} páginas sin extraer se omiten: {', '.join(missing[:20])}...")

    overrides = load_overrides()
    chain_log: list[str] = []
    merge_log: list[str] = []
    groups = _merge(_chain(pages, overrides, chain_log), overrides, merge_log)

    clusters = []
    for group in groups:  # groups keep binder order: chains are created in page order
        refs = [r for c in group for r in c["refs"]]
        clusters.append(
            {
                "id": refs[0],
                "kind": group[0]["kind"],
                "title": next((c["display"] for c in group if c["display"]), ""),
                "refs": refs,
                "pages": list(dict.fromkeys(r.split("#")[0] for r in refs)),
            }
        )
    write_json(CLUSTERS_FILE, clusters)
    write_review_section("Agrupación", chain_log + [""] + merge_log)

    recipes = sum(c["kind"] == "recipe" for c in clusters)
    multi = sum(len(c["refs"]) > 1 for c in clusters)
    print(f"{len(clusters)} grupos: {recipes} recetas, {len(clusters) - recipes} consejos; {multi} con varias partes")
