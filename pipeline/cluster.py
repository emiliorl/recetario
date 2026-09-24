"""Step 3: group page items into recipes (entity resolution). No API calls.

A page can hold several recipes, so the unit is an item, referenced as "157#2"
(second item on page 157). A bare page label like "157" means its first item.

1. Chain continuation items onto the recipe that precedes them in the binder.
2. Merge chains whose titles are near-identical (duplicate copies of a dish).
3. Apply manual fixes from data/overrides.yaml.
"""

import re
import unicodedata
from itertools import combinations

import yaml
from rapidfuzz import fuzz

from .config import AUTO_MERGE_SCORE, CLUSTERS_FILE, OVERRIDES_FILE, REVIEW_MERGE_SCORE
from .extract import cache_path
from .pages import list_pages
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
                continue
            if continues and item_ref not in split:
                log.append(f"- {item_ref}: continuación sin receta previa; queda como fragmento")
            chains.append({"title": title, "display": item["title"], "kind": kind, "refs": [item_ref]})
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

    for i, j in combinations(range(len(chains)), 2):
        a, b = chains[i], chains[j]
        if not a["title"] or not b["title"] or a["kind"] != b["kind"] or frozenset((i, j)) in apart:
            continue
        score = fuzz.ratio(a["title"], b["title"])
        if score >= AUTO_MERGE_SCORE:
            parent[find(j)] = find(i)
            log.append(f"- unidas: {a['refs'][0]} {a['display']!r} + {b['refs'][0]} {b['display']!r} ({score:.0f})")
        elif fuzz.token_set_ratio(a["title"], b["title"]) >= REVIEW_MERGE_SCORE:
            log.append(
                f"- ¿misma receta? {a['refs'][0]} {a['display']!r} / {b['refs'][0]} {b['display']!r}"
                f' → si sí, añade `- ["{a["refs"][0]}", "{b["refs"][0]}"]` a merge en overrides.yaml'
            )

    for group in overrides.get("merge") or []:
        ids = [ref_to_chain[ref(r)] for r in group if ref(r) in ref_to_chain]
        for other in ids[1:]:
            parent[find(other)] = find(ids[0])

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
