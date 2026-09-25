import glob
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

pages = sorted(glob.glob("cache/pages/*.json"))

print("=== HANDWRITTEN NOTES AND METADATA AUDIT ===")
for p in pages:
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    pnum = data.get("page")
    items = data.get("items", [])
    for idx, item in enumerate(items):
        title = item.get("title", "")
        hw = item.get("handwritten_notes", [])
        steps = item.get("steps", [])
        temp = item.get("temperature", "")
        cook = item.get("cook_time", "")
        prep = item.get("prep_time", "")
        serv = item.get("servings", "")
        kind = item.get("kind", "")
        
        if hw or temp or cook or prep or serv or kind == "tip":
            print(f"Page {pnum:5} [{idx}] title='{title}' | kind='{kind}' | hw={len(hw)} | steps={len(steps)} | temp='{temp}' | cook='{cook}' | prep='{prep}' | serv='{serv}'")
