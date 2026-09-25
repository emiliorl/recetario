import json
import sys
from pathlib import Path

start_page = int(sys.argv[1]) if len(sys.argv) > 1 else 2
end_page = int(sys.argv[2]) if len(sys.argv) > 2 else 287

for i in range(start_page, end_page + 1):
    p = f"cache/pages/page_{i}.json"
    p_alt = f"cache/pages/page_{i:03d}.json"
    path = p if Path(p).exists() else p_alt
    if not Path(path).exists():
        continue
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
        for idx, item in enumerate(d.get("items", [])):
            title = item.get("title", "Sin título")
            steps = item.get("steps", [])
            temp = item.get("temperature", "")
            cook = item.get("cook_time", "")
            model = d.get("model", "")
            print(f"Page {i} (item {idx}): '{title}' | model={model} | steps={len(steps)} | temp='{temp}' | cook='{cook}'")
