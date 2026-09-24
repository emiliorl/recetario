"""Step 4: merge each cluster into one recipe (or tip) and classify it."""

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

from . import llm
from .config import CLUSTERS_FILE, CONSOLIDATE_MODEL, CONSOLIDATE_WORKERS, RECIPES_CACHE
from .extract import cache_path
from .pages import list_pages
from .store import read_json, write_json

# Item fields used only for clustering; the model doesn't need them.
_ITEM_META = {"kind", "is_continuation", "normalized_title"}


def cache_file(cluster: dict):
    return RECIPES_CACHE / f"{cluster['id'].replace('#', '_')}.json"


def _source(cluster: dict, pages_by_label) -> tuple[dict[str, dict], str]:
    parts = {}
    for item_ref in cluster["refs"]:
        label, index = item_ref.split("#")
        item = read_json(cache_path(pages_by_label[label]))["items"][int(index) - 1]
        parts[f"Página {label}, elemento {index}"] = {k: v for k, v in item.items() if k not in _ITEM_META}
    digest = hashlib.sha256(
        json.dumps([cluster["kind"], parts, CONSOLIDATE_MODEL], ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()
    return parts, digest


def _consolidate(cluster: dict, parts: dict[str, dict], digest: str) -> dict:
    fn = llm.consolidate_recipe if cluster["kind"] == "recipe" else llm.consolidate_tip
    result, _ = fn(parts)
    data = {
        "cluster": cluster["id"],
        "kind": cluster["kind"],
        "source_refs": cluster["refs"],
        "source_hash": digest,
        cluster["kind"]: result.model_dump(),
    }
    write_json(cache_file(cluster), data)
    return data


def run(force: bool = False) -> None:
    clusters = read_json(CLUSTERS_FILE)
    pages_by_label = {p.label: p for p in list_pages()}

    todo = []
    for cluster in clusters:
        parts, digest = _source(cluster, pages_by_label)
        path = cache_file(cluster)
        if force or not path.exists() or read_json(path)["source_hash"] != digest:
            todo.append((cluster, parts, digest))

    # Clusters that no longer exist (after re-clustering) leave stale files behind.
    live = {cache_file(c).name for c in clusters}
    for path in RECIPES_CACHE.glob("*.json"):
        if path.name not in live:
            path.unlink()

    print(f"Consolidando {len(todo)} de {len(clusters)} grupos ({CONSOLIDATE_MODEL})...")
    failed = []
    with ThreadPoolExecutor(CONSOLIDATE_WORKERS) as pool:
        futures = {pool.submit(_consolidate, *args): args[0] for args in todo}
        for i, future in enumerate(as_completed(futures), 1):
            cluster = futures[future]
            try:
                data = future.result()
            except Exception as exc:  # keep going; retried on the next run
                failed.append(cluster["id"])
                print(f"[{i}/{len(todo)}] {cluster['id']}: ERROR {exc}")
                continue
            item = data[cluster["kind"]]
            print(f"[{i}/{len(todo)}] {cluster['id']}: {item['title']!r} {item.get('category', '')}")
    if failed:
        print(f"Fallaron: {failed} (vuelve a ejecutar para reintentar)")
