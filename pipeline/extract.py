"""Step 2: page-level vision extraction with per-page checkpoints."""

from concurrent.futures import ThreadPoolExecutor, as_completed

from . import llm
from .config import EXTRACT_MODEL, EXTRACT_WORKERS, PAGES_CACHE
from .pages import Page, list_pages, select_pages
from .store import read_json, write_json, write_review_section


def cache_path(page: Page):
    return PAGES_CACHE / f"{page.id}.json"


def _extract(page: Page):
    extraction, usage = llm.extract_page(page.path)
    data = {"page": page.label, "file": page.path.name, "model": EXTRACT_MODEL, **extraction.model_dump()}
    write_json(cache_path(page), data)
    return data, usage


def run(page_spec: str | None = None, force: bool = False) -> None:
    todo = [p for p in select_pages(page_spec) if force or not cache_path(p).exists()]
    print(f"Extrayendo {len(todo)} páginas ({EXTRACT_MODEL})...")
    tokens_in = tokens_out = 0
    failed = []
    with ThreadPoolExecutor(EXTRACT_WORKERS) as pool:
        futures = {pool.submit(_extract, p): p for p in todo}
        for i, future in enumerate(as_completed(futures), 1):
            page = futures[future]
            try:
                data, usage = future.result()
            except Exception as exc:  # keep going; the page is retried on the next run
                failed.append(page.label)
                print(f"[{i}/{len(todo)}] página {page.label}: ERROR {exc}")
                continue
            tokens_in += usage.input_tokens
            tokens_out += usage.output_tokens
            titles = [item["title"] or "(continuación)" for item in data["items"]] or [data["skip_reason"]]
            print(f"[{i}/{len(todo)}] página {page.label}: {'; '.join(titles)}")
    print(f"{len(todo) - len(failed)} llamadas a la API, tokens: {tokens_in} entrada / {tokens_out} salida")
    if failed:
        print(f"Fallaron: {failed} (vuelve a ejecutar para reintentar)")
    report()


def report() -> None:
    """List pages the model flagged as hard to read or rotated."""
    lines = []
    for page in list_pages():
        path = cache_path(page)
        if not path.exists():
            continue
        data = read_json(path)
        problems = []
        if data["legibility"] != "good":
            problems.append(f"legibilidad {data['legibility']}")
        if data["rotation_issue"]:
            problems.append("posiblemente girada")
        if problems:
            lines.append(f"- página {page.label} ({page.path.name}): {', '.join(problems)}")
    write_review_section("Extracción", lines)
