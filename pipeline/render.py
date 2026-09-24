"""Step 5: build the static cookbook site (site/) from the consolidated recipes.

No API calls and no scans needed, so GitHub Actions runs this step to publish.
"""

import json
import re
import shutil
from html import escape
from pathlib import Path

import markdown

from . import crypto
from .cluster import load_overrides, normalize, ref
from .config import CATEGORIES, CLUSTERS_FILE, SITE_DIR
from .consolidate import cache_file
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
}


def icon(name: str) -> str:
    return (
        '<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'
    )


def slugify(title: str) -> str:
    return normalize(title).replace(" ", "-") or "sin-titulo"


def _one_line(text: str) -> str:
    return " ".join(text.split())


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


def _step_html(step: str) -> str:
    """Bold a short lead-in such as 'Para el relleno:'."""
    text = escape(_one_line(step))
    match = re.match(r"^([^:.]{3,40}):\s+(.*)$", text)
    return f"<strong>{match.group(1)}:</strong> {match.group(2)}" if match else text


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
<link rel="stylesheet" href="{root}assets/style.css">
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
<script src="{root}assets/lock.js" data-app="{root}assets/app.js"></script>
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


def _pager(prev, nxt, root: str) -> str:
    if not (prev or nxt):
        return ""

    def link(entry, cls, label):
        if not entry:
            return "<span></span>"
        title, slug = entry
        return f'<a class="{cls}" href="{root}recetas/{slug}/"><small>{label}</small>{escape(title)}</a>'

    return f'<nav class="pager">{link(prev, "prev", "Anterior")}{link(nxt, "next", "Siguiente")}</nav>'


def recipe_html(recipe: dict, pages: list[str], slug: str, prev_next: tuple) -> str:
    root = "../../"
    notes = ""
    if recipe["teacher_notes"]:
        items = "".join(f"<li>{escape(_one_line(n))}</li>" for n in recipe["teacher_notes"])
        notes = f'<aside class="sticky-note"><h2>Notas de la maestra</h2><ul>{items}</ul></aside>'

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
    <a class="eyebrow" href="{root}#{CATEGORY_SLUGS[category]}">{escape(category)}</a>
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
    </section>
  </div>
  <p class="provenance">{_pages_label(pages)}</p>
  {_pager(*prev_next, root)}
</main>"""
    return _page(f"{recipe['title']} · Recetario", body, root)


def tip_html(tip: dict, pages: list[str]) -> str:
    root = "../../"
    content = markdown.markdown("\n\n".join(tip["body"]), extensions=["tables"])
    body = f"""{_topbar(root)}
<main class="tip">
  <header class="recipe-head">
    <a class="eyebrow" href="{root}#consejos">Consejos de cocina</a>
    <h1>{escape(tip["title"])}</h1>
  </header>
  <article class="prose card">{content}</article>
  <p class="provenance">{_pages_label(pages)}</p>
</main>"""
    return _page(f"{tip['title']} · Recetario", body, root)


def _card(recipe: dict, slug: str) -> str:
    time = recipe["cook_time"] or recipe["prep_time"]
    meta = f'<span class="card-meta">{icon("cook")}{escape(_one_line(time))}</span>' if time else ""
    ingredients = (i for g in recipe["ingredient_groups"] for i in g["items"])
    haystack = normalize(" ".join([recipe["title"], recipe["category"], *recipe["tags"], *ingredients]))
    tags = "".join(f"<li>{escape(t)}</li>" for t in recipe["tags"][:3])
    return (
        f'<li class="recipe-card" data-category="{CATEGORY_SLUGS[recipe["category"]]}" '
        f'data-tags="{escape("|".join(recipe["tags"]))}" data-search="{escape(haystack)}">'
        f'<a href="recetas/{slug}/"><h3>{escape(recipe["title"])}</h3>'
        f'<div class="card-foot">{meta}<ul class="card-tags">{tags}</ul></div></a></li>'
    )


def index_html(recipes: list[tuple[dict, str]], tips: list[tuple[dict, str]]) -> str:
    by_category: dict[str, list] = {}
    for recipe, slug in recipes:
        by_category.setdefault(recipe["category"], []).append((recipe, slug))
    ordered = [name for name in CATEGORIES.values() if name in by_category]

    chips = '<button class="chip" aria-pressed="true" data-filter="">Todas</button>' + "".join(
        f'<button class="chip" aria-pressed="false" data-filter="{CATEGORY_SLUGS[n]}">{escape(n)}'
        f" <span>{len(by_category[n])}</span></button>"
        for n in ordered
    )
    all_tags = sorted({t for recipe, _ in recipes for t in recipe["tags"]}, key=normalize)
    tag_chips = "".join(
        f'<button class="tag-chip" aria-pressed="false" data-tag="{escape(t)}">{escape(t)}</button>' for t in all_tags
    )

    sections = []
    for number, name in enumerate(ordered, 1):
        cards = "".join(_card(r, s) for r, s in by_category[name])
        sections.append(
            f'<section class="chapter" id="{CATEGORY_SLUGS[name]}">'
            f'<h2><span class="chapter-no">{number:02d}</span>{escape(name)}</h2>'
            f'<ul class="card-grid">{cards}</ul></section>'
        )
    if tips:
        links = "".join(f'<li><a href="consejos/{slug}/">{escape(tip["title"])}</a></li>' for tip, slug in tips)
        sections.append(
            '<section class="chapter tips-chapter" id="consejos"><h2><span class="chapter-no">✦</span>'
            f'Consejos de cocina</h2><ul class="tip-list">{links}</ul></section>'
        )

    body = f"""<header class="masthead">
  <p class="kicker">Cuaderno de la familia</p>
  <h1>Recetario</h1>
  <p class="lede">{len(recipes)} recetas del cuaderno de clases de cocina, pasadas en limpio para tenerlas siempre a mano.</p>
  <label class="search">{icon("search")}<input type="search" placeholder="Buscar receta o ingrediente…" aria-label="Buscar receta o ingrediente"></label>
</header>
<main class="home">
  <nav class="filters" aria-label="Categorías">{chips}</nav>
  <div class="tag-filters" role="group" aria-label="Etiquetas">{tag_chips}</div>
  <p class="empty" hidden>No hay recetas que coincidan.</p>
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
        entry = (item, crypto.opaque_id(_unique(slugify(item["title"]), used)), cluster["pages"])
        (recipes if data["kind"] == "recipe" else tips).append(entry)

    order = list(CATEGORIES.values())
    recipes.sort(key=lambda e: (order.index(e[0]["category"]), normalize(e[0]["title"])))
    tips.sort(key=lambda e: normalize(e[0]["title"]))

    shutil.rmtree(SITE_DIR, ignore_errors=True)
    shutil.copytree(ASSETS_DIR, SITE_DIR / "assets")

    def neighbour(i, category):
        if 0 <= i < len(recipes) and recipes[i][0]["category"] == category:
            return recipes[i][0]["title"], recipes[i][1]
        return None

    for i, (recipe, slug, pages) in enumerate(recipes):
        pager = (neighbour(i - 1, recipe["category"]), neighbour(i + 1, recipe["category"]))
        _write(SITE_DIR / "recetas" / slug / "index.html", recipe_html(recipe, pages, slug, pager))
    for tip, slug, pages in tips:
        _write(SITE_DIR / "consejos" / slug / "index.html", tip_html(tip, pages))
    _write(SITE_DIR / "index.html", index_html([(r, s) for r, s, _ in recipes], [(t, s) for t, s, _ in tips]))
    _write(SITE_DIR / ".nojekyll", "")
    _write(SITE_DIR / "robots.txt", "User-agent: *\nDisallow: /\n")
    print(f"Sitio generado en {SITE_DIR}: {len(recipes)} recetas, {len(tips)} consejos")


def serve(port: int = 8000) -> None:
    """Preview locally; a phone on the same Wi-Fi can open http://<this-pc-ip>:8000."""
    import functools
    import http.server

    if not (SITE_DIR / "index.html").exists():
        run()
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(SITE_DIR))
    print(f"Sirviendo {SITE_DIR} en http://localhost:{port} (Ctrl+C para salir)")
    http.server.ThreadingHTTPServer(("0.0.0.0", port), handler).serve_forever()
