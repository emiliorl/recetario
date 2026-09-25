"""Step 5: build the static cookbook site (site/) from the consolidated recipes.

No API calls and no scans needed, so GitHub Actions runs this step to publish.
"""

import hashlib
import json
import re
import shutil
from html import escape
from pathlib import Path

import markdown

from . import crypto
from .cluster import load_overrides, normalize, ref
from .config import (
    CATEGORIES,
    CLUSTERS_FILE,
    MAX_TIPS_PER_RECIPE,
    SCANS_DIR,
    SITE_DIR,
    TAG_ALIASES,
    TAG_GROUPS,
    TIP_LINKS,
)
from .consolidate import cache_file
from .scans import scan_name
from .store import read_json

ASSETS_DIR = Path(__file__).parent / "assets"
CATEGORY_SLUGS = {name: slug for slug, name in CATEGORIES.items()}
FONTS = (
    "https://fonts.googleapis.com/css2?family=Caveat:wght@500;700"
    "&family=Fraunces:ital,opsz,wght@0,9..144,400..800;1,9..144,400..700"
    "&family=Lora:ital,wght@0,400..600;1,400&display=swap"
)

ICONS = {
    "servings": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/>',
    "prep": '<path d="M6 13.87A4 4 0 0 1 7.41 6a5.11 5.11 0 0 1 1.05-1.54 5 5 0 0 1 7.08 0A5.11 5.11 0 0 1 16.59 6 4 4 0 0 1 18 13.87V21H6Z"/><path d="M6 17h12"/>',
    "cook": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "oven": '<path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/>',
    "back": '<path d="m15 18-6-6 6-6"/>',
    "book": '<path d="M2 4h6a4 4 0 0 1 4 4v13a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v13a3 3 0 0 1 3-3h7z"/>',
    "list": '<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
    "external": '<path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
    "sliders": '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M1 14h6M9 8h6M17 16h6"/>',
}


def _asset(root: str, name: str) -> str:
    """URL with a content hash, so browsers pick up a new style.css/app.js right after a deploy."""
    digest = hashlib.sha256((ASSETS_DIR / name).read_bytes()).hexdigest()[:10]
    return f"{root}assets/{name}?v={digest}"


def icon(name: str) -> str:
    return (
        '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
    )


def slugify(title: str) -> str:
    return normalize(title).replace(" ", "-") or "sin-titulo"


def _one_line(text: str) -> str:
    return " ".join(text.split())


# Course credits ("Cátedra de Arte Culinario, Hogar Empresa II del IFES...") the model files as notes.
CREDIT_RE = re.compile(
    r"c[aá]tedr|hogar empresa|\bIFES\b|margarita de s[aá]nchez|instituto femenino", re.IGNORECASE
)


def _strip_credits(note: str) -> str:
    """Drops the sentences that only credit the course, keeping any real tip in the same note."""
    sentences = re.split(r"(?<=\.)\s+", _one_line(note))
    return " ".join(s for s in sentences if not CREDIT_RE.search(s))


def _label_key(label: str) -> tuple[int, int]:
    number, _, sub = label.partition("-")
    return int(number), int(sub or 0)


def _page_range(pages: list[str]) -> str:
    """["9", "10", "11", "40"] -> "9–11, 40". "157-1" (an extra scan) counts as right after "157"."""
    ordered = sorted(set(pages), key=_label_key)
    parts, start = [], ordered[0]
    for prev, cur in zip(ordered, ordered[1:] + [None]):
        n, s = _label_key(prev)
        if cur is None or _label_key(cur) not in ((n, s + 1), (n + 1, 0)):
            parts.append(start if start == prev else f"{start}–{prev}")
            start = cur
    return ", ".join(parts)


def _pages_label(pages: list[str]) -> str:
    return f"Del cuaderno · {'página' if len(pages) == 1 else 'páginas'} {_page_range(pages)}"


def _sources(pages: list[str], root: str) -> str:
    """The page numbers, opening onto the scans themselves so anyone can check the recipe against them.

    app.js fetches and decrypts the images only when this is opened.
    """
    label = f'<p class="provenance">{_pages_label(pages)}</p>'
    figures = "".join(
        f'<figure><a class="scan" target="_blank" data-src="{root}scans/{scan_name(page)}">'
        f'<img alt="Página {page} del cuaderno" hidden></a><figcaption>Página {page}</figcaption></figure>'
        for page in sorted(set(pages), key=_label_key)
        if (SCANS_DIR / scan_name(page)).exists()
    )
    if not figures:
        return label
    return (
        f'<details class="sources"><summary>{label}<span class="sources-open">Ver el original</span></summary>'
        '<p class="hint">Compara con la página escrita si algo no cuadra. Toca una página para verla en grande.</p>'
        f'<div class="scans">{figures}</div></details>'
    )


def _step_html(step: str) -> str:
    """Bold a short lead-in such as 'Para el relleno:'."""
    text = escape(_one_line(step))
    match = re.match(r"^([^:.]{3,40}):\s+(.*)$", text)
    return f"<strong>{match.group(1)}:</strong> {match.group(2)}" if match else text


def _plain(md: str) -> str:
    """Markdown -> one line of plain text, for excerpts, word counts and search."""
    return _one_line(re.sub(r"[*_`#>|]", " ", md))


def _markdown(md: str) -> str:
    # Python-Markdown nests lists only at 4-space indents; the notebook text uses 2 or 3.
    md = re.sub(r"^( +)(?=(?:[*+-]|\d+\.)\s)", lambda m: m.group(1) * 2, md, flags=re.M)
    return markdown.markdown(md, extensions=["tables"])


def _tip_parts(tip: dict) -> tuple[str, list[tuple[str, str]]]:
    """Split a tip into its intro and (heading, markdown) sections at each '###' heading."""
    chunks = re.split(r"^#{1,4}\s+(.+?)\s*#*\s*$", "\n\n".join(tip["body"]), flags=re.M)
    sections = [(_plain(h), md.strip()) for h, md in zip(chunks[1::2], chunks[2::2])]
    return chunks[0].strip(), sections


def _reading_minutes(tip: dict) -> int:
    return max(1, round(len(_plain(" ".join(tip["body"])).split()) / 180))


def _page(title: str, body: str, root: str, body_class: str = "") -> str:
    """A password screen; the real page travels encrypted and lock.js decrypts it in the browser.

    Nothing readable (not even the title) is in the published HTML.
    """
    payload = crypto.encrypt_page(json.dumps({"title": title, "cls": body_class, "body": body}, ensure_ascii=False))
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Recetario</title>
<meta name="theme-color" content="#f7f1e6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#1d1815" media="(prefers-color-scheme: dark)">
<link rel="icon" href="{root}assets/icon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{_asset(root, 'style.css')}">
</head>
<body class="locked">
<main class="lock-screen">
  <form class="lock-card">
    <p class="kicker">Cuaderno de la familia</p>
    <h1>Recetario</h1>
    <p class="lock-text">Este recetario es solo para la familia. Escribe la contraseña para entrar.</p>
    <input type="password" name="password" autocomplete="current-password" placeholder="Contraseña" aria-label="Contraseña" required>
    <label class="remember"><input type="checkbox" checked> Recordar en este dispositivo</label>
    <button type="submit">Entrar</button>
    <p class="lock-error" role="alert" hidden>Contraseña incorrecta.</p>
  </form>
  <noscript><p class="lock-text">Activa JavaScript para abrir el recetario.</p></noscript>
</main>
<script id="payload" type="application/octet-stream" data-salt="{crypto.SITE_SALT.decode()}" data-iterations="{crypto.PBKDF2_ITERATIONS}">{payload}</script>
<script src="{_asset(root, 'lock.js')}" data-app="{_asset(root, 'app.js')}"></script>
</body>
</html>
"""


def _topbar(root: str) -> str:
    return f'<header class="topbar"><a class="back" href="{root}">{icon("back")}<span>Recetario</span></a></header>'


def _facts(recipe: dict) -> str:
    facts = [
        ("servings", "Porciones", recipe["servings"]),
        ("prep", "Preparación", recipe["prep_time"]),
        ("cook", "Cocción", recipe["cook_time"]),
        ("oven", "Horno", recipe["temperature"]),
    ]
    items = "".join(
        f'<div class="fact">{icon(key)}<div><dt>{label}</dt><dd>{escape(_one_line(value))}</dd></div></div>'
        for key, label, value in facts
        if value
    )
    return f'<dl class="facts">{items}</dl>' if items else ""


def _tags(tags: list[str]) -> str:
    if not tags:
        return ""
    return '<ul class="tags">' + "".join(f"<li>{escape(t)}</li>" for t in tags) + "</ul>"


def _pager(prev, nxt, root: str, folder: str = "recetas") -> str:
    if not (prev or nxt):
        return ""

    def link(entry, cls, label):
        if not entry:
            return "<span></span>"
        title, slug = entry
        return f'<a class="{cls}" href="{root}{folder}/{slug}/"><small>{label}</small>{escape(title)}</a>'

    return f'<nav class="pager">{link(prev, "prev", "Anterior")}{link(nxt, "next", "Siguiente")}</nav>'


def _related_tips(tips: list[tuple[dict, str]]) -> str:
    """Opens in a new tab so the recipe (and its ticked steps, saved anyway) stays where it was."""
    if not tips:
        return ""
    cards = "".join(
        f'<li><a href="../../consejos/{slug}/" target="_blank" rel="noopener">{icon("book")}'
        f'<span><strong>{escape(tip["title"])}</strong><small>{_reading_minutes(tip)} min de lectura</small></span>'
        f'{icon("external")}</a></li>'
        for tip, slug in tips
    )
    return (
        '<section class="related"><h2>Consejos para esta receta</h2>'
        '<p class="hint">Se abren en otra pestaña; lo que marcaste aquí queda guardado.</p>'
        f'<ul class="related-list">{cards}</ul></section>'
    )


def recipe_html(recipe: dict, pages: list[str], slug: str, prev_next: tuple, tips: list) -> str:
    root = "../../"
    notes = ""
    teacher_notes = [n for n in map(_strip_credits, recipe["teacher_notes"]) if n]
    if teacher_notes:
        items = "".join(f"<li>{escape(n)}</li>" for n in teacher_notes)
        notes = f'<aside class="sticky-note"><h2>Notas</h2><ul>{items}</ul></aside>'

    groups = []
    for group in recipe["ingredient_groups"]:
        heading = f"<h3>{escape(_one_line(group['name']))}</h3>" if group["name"] else ""
        items = "".join(
            f'<li><label><input type="checkbox"><span>{escape(_one_line(item))}</span></label></li>'
            for item in group["items"]
        )
        groups.append(f'{heading}<ul class="checklist">{items}</ul>')

    steps = "".join(f'<li class="step" tabindex="0"><p>{_step_html(s)}</p></li>' for s in recipe["steps"])
    extra_notes = ""
    if recipe["notes"]:
        items = "".join(f"<li>{escape(_one_line(n))}</li>" for n in recipe["notes"])
        extra_notes = f'<section class="notes"><h2>Notas</h2><ul>{items}</ul></section>'

    category = recipe["category"]
    body = f"""{_topbar(root)}
<main class="recipe" data-recipe="{slug}">
  <header class="recipe-head">
    <a class="eyebrow" href="{root}?c={CATEGORY_SLUGS[category]}">{escape(category)}</a>
    <h1>{escape(recipe["title"])}</h1>
    {_facts(recipe)}
    {_tags(recipe["tags"])}
  </header>
  {notes}
  <div class="toolbar">
    <button class="wake" type="button" hidden aria-pressed="false">{icon("sun")}<span>Mantener pantalla encendida</span></button>
    <button class="reset" type="button" hidden>Desmarcar todo</button>
  </div>
  <div class="recipe-body">
    <section class="ingredients card">
      <h2>Ingredientes</h2>
      {"".join(groups)}
    </section>
    <section class="method">
      <h2>Procedimiento</h2>
      <p class="hint">Toca un paso para marcarlo como hecho.</p>
      <ol class="steps">{steps}</ol>
      {extra_notes}
      {_related_tips(tips)}
    </section>
  </div>
  {_sources(pages, root)}
  {_pager(*prev_next, root)}
</main>"""
    return _page(f"{recipe['title']} · Recetario", body, root)


def _used_in(recipes: list[tuple[dict, str]], root: str) -> str:
    if not recipes:
        return ""
    links = "".join(
        f'<li><a href="{root}recetas/{slug}/"><small>{escape(r["category"])}</small>{escape(r["title"])}</a></li>'
        for r, slug in recipes
    )
    return f'<section class="used-in"><h2>Recetas donde sirve</h2><ul>{links}</ul></section>'


def tip_html(tip: dict, pages: list[str], prev_next: tuple, recipes: list) -> str:
    """Laid out like a recipe: facts under the title, a sticky contents card, numbered sections."""
    root = "../../"
    intro, sections = _tip_parts(tip)
    facts = [("book", "Lectura", f"{_reading_minutes(tip)} min")]
    if len(sections) > 1:
        facts.append(("list", "Temas", str(len(sections))))
    facts_html = "".join(
        f'<div class="fact">{icon(key)}<div><dt>{label}</dt><dd>{value}</dd></div></div>' for key, label, value in facts
    )
    lede = f'<div class="tip-intro">{_markdown(intro)}</div>' if intro else ""

    blocks = "".join(
        f'<section class="tip-section" id="tema-{n}"><h2><span class="chapter-no">{n:02d}</span>{escape(heading)}</h2>'
        f'<div class="prose">{_markdown(md)}</div></section>'
        for n, (heading, md) in enumerate(sections, 1)
    )
    if len(sections) > 1:
        links = "".join(f'<li><a href="#tema-{n}">{escape(h)}</a></li>' for n, (h, _) in enumerate(sections, 1))
        toc = f'<nav class="toc card" aria-label="En esta página"><h2>En esta página</h2><ol>{links}</ol></nav>'
        content = f'<div class="recipe-body tip-body">{toc}<div class="tip-sections">{blocks}</div></div>'
    else:
        content = f'<div class="tip-sections solo">{blocks}</div>'

    body = f"""{_topbar(root)}
<main class="tip">
  <header class="recipe-head">
    <a class="eyebrow" href="{root}?c=consejos">Consejos de cocina</a>
    <h1>{escape(tip["title"])}</h1>
    {lede}
    <dl class="facts">{facts_html}</dl>
  </header>
  {content}
  {_used_in(recipes, root)}
  {_sources(pages, root)}
  {_pager(*prev_next, root, "consejos")}
</main>"""
    return _page(f"{tip['title']} · Recetario", body, root)


def _card(recipe: dict, slug: str) -> str:
    time = recipe["cook_time"] or recipe["prep_time"]
    meta = f'<span class="card-meta">{icon("cook")}{escape(_one_line(time))}</span>' if time else ""
    ingredients = (i for g in recipe["ingredient_groups"] for i in g["items"])
    haystack = normalize(" ".join([recipe["title"], recipe["category"], *recipe["tags"], *ingredients]))
    tags = "".join(f"<li>{escape(t)}</li>" for t in recipe["tags"][:3])
    lines = (_one_line(i) for g in recipe["ingredient_groups"] for i in g["items"])
    return (
        f'<li class="recipe-card" data-category="{CATEGORY_SLUGS[recipe["category"]]}" '
        f'data-tags="{escape("|".join(recipe["tags"]))}" data-search="{escape(haystack)}" '
        f'data-title="{escape(normalize(recipe["title"]))}" data-ingredients="{escape("|".join(lines))}">'
        f'<a href="recetas/{slug}/"><h3>{escape(recipe["title"])}</h3>'
        f'<p class="card-match" hidden></p>'
        f'<div class="card-foot">{meta}<ul class="card-tags">{tags}</ul></div></a></li>'
    )


def _tip_card(tip: dict, slug: str) -> str:
    intro, sections = _tip_parts(tip)
    if intro:
        text = _plain(intro)
        excerpt = (re.match(r"(.+?[.!?])(\s|$)", text) or re.match(r"(.+)", text)).group(1)
    else:
        excerpt = " · ".join(h for h, _ in sections)
    topics = f" · {len(sections)} temas" if len(sections) > 1 else ""
    haystack = normalize(" ".join([tip["title"], _plain(" ".join(tip["body"]))]))
    return (
        f'<li class="recipe-card tip-card" data-category="consejos" data-tags="" data-search="{escape(haystack)}">'
        f'<a href="consejos/{slug}/"><h3>{escape(tip["title"])}</h3>'
        f'<p class="card-excerpt">{escape(excerpt)}</p>'
        f'<div class="card-foot"><span class="card-meta">{icon("book")}{_reading_minutes(tip)} min de lectura{topics}</span>'
        f"</div></a></li>"
    )


def _tag_panel(recipes: list[tuple[dict, str]]) -> str:
    counts: dict[str, int] = {}
    for recipe, _ in recipes:
        for tag in recipe["tags"]:
            counts[tag] = counts.get(tag, 0) + 1
    used = {t for t, n in counts.items() if n > 1}  # one-off tags stay on the recipe but don't earn a filter
    grouped = {name: [t for t in tags if t in used] for name, tags in TAG_GROUPS.items()}
    listed = {t for tags in grouped.values() for t in tags}
    grouped["Otras"] = sorted(used - listed, key=normalize)

    groups = "".join(
        f'<div class="tag-group"><h3>{escape(name)}</h3><div class="tag-list">'
        + "".join(
            f'<button class="tag-chip" type="button" aria-pressed="false" data-tag="{escape(t)}">'
            f"{escape(t)} <span>{counts[t]}</span></button>"
            for t in tags
        )
        + "</div></div>"
        for name, tags in grouped.items()
        if tags
    )
    return f'<div class="tag-panel" id="tag-panel" hidden>{groups}</div>'


def index_html(recipes: list[tuple[dict, str]], tips: list[tuple[dict, str]]) -> str:
    by_category: dict[str, list] = {}
    for recipe, slug in recipes:
        by_category.setdefault(recipe["category"], []).append((recipe, slug))
    ordered = [name for name in CATEGORIES.values() if name in by_category]

    def chip(value: str, label: str, count: int) -> str:
        return (
            f'<button class="chip" type="button" aria-pressed="{str(not value).lower()}" data-filter="{value}">'
            f"{escape(label)} <span>{count}</span></button>"
        )

    chips = chip("", "Todas", len(recipes)) + "".join(
        chip(CATEGORY_SLUGS[n], n, len(by_category[n])) for n in ordered
    )
    if tips:
        chips += chip("consejos", "Consejos", len(tips))

    sections = []
    for number, name in enumerate(ordered, 1):
        cards = "".join(_card(r, s) for r, s in by_category[name])
        sections.append(
            f'<section class="chapter" id="{CATEGORY_SLUGS[name]}">'
            f'<h2><span class="chapter-no">{number:02d}</span>{escape(name)}</h2>'
            f'<ul class="card-grid">{cards}</ul></section>'
        )
    if tips:
        cards = "".join(_tip_card(t, s) for t, s in tips)
        sections.append(
            '<section class="chapter tips-chapter" id="consejos"><h2><span class="chapter-no">✦</span>'
            f'Consejos de cocina</h2><ul class="card-grid">{cards}</ul></section>'
        )

    tips_note = f" y {len(tips)} consejos" if tips else ""
    body = f"""<header class="masthead">
  <p class="kicker">Cuaderno de la familia</p>
  <h1>Recetario</h1>
  <p class="lede">{len(recipes)} recetas{tips_note} del cuaderno de clases de cocina, pasadas en limpio para tenerlas siempre a mano.</p>
</header>
<div class="finder">
  <div class="finder-row">
    <label class="search">{icon("search")}<input type="search" placeholder="Receta o ingrediente…" aria-label="Buscar receta o ingrediente" enterkeyhint="search"></label>
    <button class="filter-toggle" type="button" aria-expanded="false" aria-controls="tag-panel">{icon("sliders")}<span>Filtros</span><span class="badge" hidden></span></button>
  </div>
  <nav class="filters" aria-label="Categorías">{chips}</nav>
  {_tag_panel(recipes)}
</div>
<main class="home">
  <div class="results-bar"><p class="count" aria-live="polite"></p><button class="clear" type="button" hidden>Limpiar filtros</button></div>
  <div class="empty" hidden><p>No hay nada que coincida.</p><button class="clear" type="button">Limpiar filtros</button></div>
  {"".join(sections)}
</main>
<footer class="site-footer">Pasado en limpio del cuaderno original.
  <button class="lock-out" type="button">Cerrar sesión en este dispositivo</button></footer>"""
    return _page("Recetario", body, "", "home")


def _unique(slug: str, used: set[str]) -> str:
    candidate, i = slug, 2
    while candidate in used:
        candidate, i = f"{slug}-{i}", i + 1
    used.add(candidate)
    return candidate


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _matches(text: str, words: list[str]) -> int:
    return sum(bool(re.search(rf"\b{re.escape(w)}(?:e?s)?\b", text)) for w in words)


def _link_tips(recipes: list, tips: list) -> dict[str, list]:
    """Recipe slug -> the consejos worth reading for it, best match first (see TIP_LINKS)."""
    rules = []
    for key, rule in TIP_LINKS.items():
        found = [(t, s) for t, s, _ in tips if normalize(key) in normalize(t["title"])]
        if not found:
            print(f"Aviso: TIP_LINKS['{key}'] no coincide con ningún consejo")
        rules += [(tip, slug, rule) for tip, slug in found]

    links = {}
    for recipe, slug, _ in recipes:
        title = normalize(recipe["title"])
        body = normalize(" ".join([*recipe["steps"], *(i for g in recipe["ingredient_groups"] for i in g["items"])]))
        scored = []
        for n, (tip, tip_slug, rule) in enumerate(rules):
            if recipe["category"] in rule.get("skip", []):
                continue
            score = 3 * _matches(title, rule.get("title", [])) + _matches(body, rule.get("body", []))
            if score:
                scored.append((-score, n, tip, tip_slug))
        links[slug] = [(tip, tip_slug) for *_, tip, tip_slug in sorted(scored)[:MAX_TIPS_PER_RECIPE]]
    return links


def _apply_fix(item: dict, fix: dict) -> dict:
    return {**item, **{k: v for k, v in fix.items() if k in item}}


def run() -> None:
    fixes = {ref(k): v for k, v in (load_overrides().get("fix") or {}).items()}
    used: set[str] = set()
    recipes, tips = [], []
    for cluster in read_json(CLUSTERS_FILE):
        path = cache_file(cluster)
        if not path.exists():
            print(f"Aviso: {cluster['id']} sin consolidar, se omite")
            continue
        data = read_json(path)
        item = _apply_fix(data[data["kind"]], fixes.get(cluster["id"], {}))
        if "tags" in item:
            item["tags"] = list(dict.fromkeys(TAG_ALIASES.get(t, t) for t in item["tags"]))
        entry = (item, crypto.opaque_id(_unique(slugify(item["title"]), used)), cluster["pages"])
        (recipes if data["kind"] == "recipe" else tips).append(entry)

    order = list(CATEGORIES.values())
    recipes.sort(key=lambda e: (order.index(e[0]["category"]), normalize(e[0]["title"])))
    tips.sort(key=lambda e: normalize(e[0]["title"]))

    shutil.rmtree(SITE_DIR, ignore_errors=True)
    shutil.copytree(ASSETS_DIR, SITE_DIR / "assets")
    if SCANS_DIR.exists():
        shutil.copytree(SCANS_DIR, SITE_DIR / "scans")

    def neighbour(i, category):
        if 0 <= i < len(recipes) and recipes[i][0]["category"] == category:
            return recipes[i][0]["title"], recipes[i][1]
        return None

    tip_links = _link_tips(recipes, tips)
    for i, (recipe, slug, pages) in enumerate(recipes):
        pager = (neighbour(i - 1, recipe["category"]), neighbour(i + 1, recipe["category"]))
        _write(SITE_DIR / "recetas" / slug / "index.html", recipe_html(recipe, pages, slug, pager, tip_links[slug]))
    for i, (tip, slug, pages) in enumerate(tips):
        pager = tuple((tips[j][0]["title"], tips[j][1]) if 0 <= j < len(tips) else None for j in (i - 1, i + 1))
        used_in = [(r, s) for r, s, _ in recipes if any(t_slug == slug for _, t_slug in tip_links[s])]
        _write(SITE_DIR / "consejos" / slug / "index.html", tip_html(tip, pages, pager, used_in))
    _write(SITE_DIR / "index.html", index_html([(r, s) for r, s, _ in recipes], [(t, s) for t, s, _ in tips]))
    _write(SITE_DIR / ".nojekyll", "")
    _write(SITE_DIR / "robots.txt", "User-agent: *\nDisallow: /\n")
    linked = sum(bool(v) for v in tip_links.values())
    print(f"Sitio generado en {SITE_DIR}: {len(recipes)} recetas, {len(tips)} consejos ({linked} recetas con consejos)")


def serve(port: int = 8000) -> None:
    """Preview locally; a phone on the same Wi-Fi can open http://<this-pc-ip>:8000."""
    import functools
    import http.server

    if not (SITE_DIR / "index.html").exists():
        run()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE_DIR))
    print(f"Sirviendo {SITE_DIR} en http://localhost:{port} (Ctrl+C para salir)")
    http.server.ThreadingHTTPServer(("0.0.0.0", port), handler).serve_forever()
