import glob
import json
import re

pages = sorted(glob.glob("cache/pages/page_*.json"))
flagged_pages = []

hallucination_triggers = [
    r"precalent",
    r"engrasar\s+y\s+enharinar",
    r"350\s*°",
    r"180\s*°",
    r"servir\s+(caliente|frío|de inmediato)",
    r"disfrut",
    r"molde.*engrasad",
]

for p in pages:
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)

    page_num = data.get("page")
    items = data.get("items", [])
    page_flags = []

    for idx, item in enumerate(items):
        title = item.get("title", "Sin título")
        temp = item.get("temperature", "")
        cook = item.get("cook_time", "")
        prep = item.get("prep_time", "")
        serv = item.get("servings", "")
        steps = item.get("steps", [])

        if temp:
            page_flags.append(f"item[{idx}] '{title}' has temperature: '{temp}'")
        if cook:
            page_flags.append(f"item[{idx}] '{title}' has cook_time: '{cook}'")

        steps_text = " ".join(steps).lower()
        for trig in hallucination_triggers:
            m = re.search(trig, steps_text)
            if m:
                page_flags.append(f"item[{idx}] '{title}' step trigger: '{m.group(0)}'")

    if page_flags:
        flagged_pages.append((p, page_num, page_flags))

print(f"Total pages flagged for potential hallucinated defaults: {len(flagged_pages)} / {len(pages)}")
for p, num, flags in flagged_pages:
    print(f"Page {num} ({p}):")
    for fl in flags:
        print(f"  - {fl}")
