import glob
import json
import re
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from pipeline.source import Source  # noqa: E402

# Page extractions come in three ingredient shapes: flat "ingredients" (list of
# strings), "ingredient_groups"/"items" (list of strings) and "ingredient_groups"/
# "ingredients" (list of structured {name, amount, unit} dicts). pipeline/source.py
# already parses all three (it's what `pipeline verify` checks against), so reuse
# it here instead of re-deriving ingredient text by hand.
def item_ingredient_groups(it: dict) -> list[dict]:
    source = Source()
    source.add(it)
    seen, group_items = set(), []
    for line in source.ingredients:
        if line not in seen:
            seen.add(line)
            group_items.append(line)
    return [{"name": "", "items": group_items}] if group_items else []

# Load config taxonomy
CATEGORIES = [
    "Panes y masas",
    "Postres y pasteles",
    "Platos principales",
    "Sopas y cremas",
    "Entradas y bocadillos",
    "Salsas y aderezos",
    "Básicos y rellenos",
    "Bebidas",
]

TAGS = [
    "rápido",
    "desayuno",
    "levadura",
    "horneado",
    "sin horno",
    "frito",
    "guiso",
    "festivo",
    "chocolate",
    "frutas",
    "baño maría",
    "congelable",
    "vegetariano",
    "carne",
    "pollo",
    "pescado y mariscos",
]

def classify_recipe(title: str, ingredients_text: str, steps_text: str) -> tuple[str, list[str]]:
    t_lower = title.lower()
    all_text = f"{title} {ingredients_text} {steps_text}".lower()

    # Category determination
    if any(w in t_lower for w in ["sopa", "caldo", "consomé", "consome", "crema de"]):
        category = "Sopas y cremas"
    elif any(w in t_lower for w in ["batido", "bebida", "café", "cafe", "egg nog", "ponche", "jugo", "refresco"]):
        category = "Bebidas"
    elif any(w in t_lower for w in ["salsa", "aderezo", "vinagreta", "mayonesa", "chutney"]):
        category = "Salsas y aderezos"
    elif any(w in t_lower for w in ["betún", "betun", "escarcha", "relleno", "cobertura", "baño de", "bano de", "pasta laminada", "glass"]):
        category = "Básicos y rellenos"
    elif any(w in t_lower for w in ["pan de", "pretzels", "pretzel", "masa para"]):
        category = "Panes y masas"
    elif any(w in t_lower for w in ["bocadillo", "canapé", "canape", "dip", "tostaditas", "nachos", "champiñones rellenos", "aperitivos"]):
        category = "Entradas y bocadillos"
    elif any(w in t_lower for w in [
        "pie", "pastel", "torta", "brownie", "chiffón", "chiffon", "brazo", "flan", "gelatina", "galleta",
        "turrón", "turron", "postre", "crepes dulce", "cupcake", "cheesecake", "strudel", "struddel",
        "jalousie", "tiramisú", "tiramisu", "eclairs", "pastería"
    ]):
        category = "Postres y pasteles"
    elif any(w in t_lower for w in [
        "pollo", "carne", "lomo", "lomito", "pavo", "pescado", "robalo", "camarón", "camaron", "mariscos",
        "lasagna", "lasaña", "arroz", "espaghetti", "spaghetti", "fusilli", "roast beef", "quiche", "enchiladas",
        "tacos", "burrito", "ratatouille", "medallones", "cazerola", "cacerola", "souffle", "soufflé",
        "huevos", "omelette", "jamón", "jamon", "frijoles", "papas", "verduras", "alitas", "zucchini"
    ]):
        category = "Platos principales"
    else:
        # Fallback based on ingredients
        if any(w in all_text for w in ["azúcar", "azucar", "chocolate", "vainilla", "harina"]):
            category = "Postres y pasteles"
        else:
            category = "Platos principales"

    # Tags selection (0 to 4)
    tags = []
    if "chocolate" in all_text or "cocoa" in all_text:
        tags.append("chocolate")
    if any(w in all_text for w in ["manzana", "limón", "limon", "naranja", "fresa", "frambuesa", "fruta", "ciruela", "maracuyá", "maracuya", "albaricoque"]):
        tags.append("frutas")
    if "horno" in all_text or "hornear" in all_text or "350" in all_text or "180" in all_text:
        tags.append("horneado")
    elif "frito" in all_text or "freír" in all_text or "freir" in all_text:
        tags.append("frito")
    elif "baño maría" in all_text or "baño maria" in all_text or "bano maria" in all_text:
        tags.append("baño maría")

    if "pollo" in all_text:
        tags.append("pollo")
    elif any(w in all_text for w in ["carne", "lomo", "lomito", "res", "ternera"]):
        tags.append("carne")
    elif any(w in all_text for w in ["pescado", "camarón", "camaron", "marisco", "robalo"]):
        tags.append("pescado y mariscos")

    if any(w in t_lower for w in ["navideño", "navideno", "navidad", "fiesta"]):
        tags.append("festivo")

    # Limit to 4 tags max
    tags = list(dict.fromkeys(tags))[:4]
    return category, tags

def main():
    pages_by_label = {}
    for path in glob.glob("cache/pages/*.json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        pages_by_label[str(data["page"])] = data

    clusters = json.load(open("cache/clusters.json", "r", encoding="utf-8"))
    print(f"Building {len(clusters)} consolidated recipes/tips from cache/pages...")

    built_count = 0
    for cluster in clusters:
        cid = cluster["id"]
        refs = cluster["refs"]
        kind = cluster["kind"]

        # Gather source parts
        items = []
        for ref in refs:
            label, idx_str = ref.split("#")
            page_data = pages_by_label.get(label)
            if not page_data:
                continue
            idx = int(idx_str) - 1
            if idx < len(page_data["items"]):
                items.append((label, page_data["items"][idx]))

        if not items:
            continue

        first_item = items[0][1]
        title = first_item.get("title", "").strip()
        if not title:
            # Fallback to non-empty title in subsequent items if continuation
            for _, it in items:
                if it.get("title", "").strip():
                    title = it.get("title", "").strip()
                    break

        if kind == "tip":
            body = []
            for _, it in items:
                for grp in item_ingredient_groups(it):
                    if grp.get("name"):
                        body.append(f"### {grp['name']}")
                    for ing in grp.get("items", []):
                        body.append(f"- {ing}")
                for st in it.get("steps", []):
                    body.append(st)
                for hw in it.get("handwritten_notes", []):
                    body.append(f"> *Nota a mano:* {hw}")
                item_notes = it.get("notes") or []
                if isinstance(item_notes, str):
                    item_notes = [item_notes]
                for n in item_notes:
                    body.append(f"*Nota:* {n}")

            tip_data = {
                "title": title or "Consejo de cocina",
                "body": body if body else ["Sin contenido adicional."]
            }
            rec_obj = {
                "cluster": cid,
                "kind": "tip",
                "source_refs": refs,
                "source_hash": "verbatim_clean_v1",
                "tip": tip_data
            }
        else:
            # Recipe consolidation
            servings = first_item.get("servings", "")
            prep_time = first_item.get("prep_time", "")
            cook_time = first_item.get("cook_time", "")
            temperature = first_item.get("temperature", "")

            # Combine ingredient groups, steps, teacher_notes, notes
            ingredient_groups = []
            steps = []
            teacher_notes = []
            notes = []

            for _, it in items:
                # Merge ingredient groups.
                for grp in item_ingredient_groups(it):
                    gname = grp.get("name", "")
                    gitems = [i for i in grp.get("items", []) if i.strip()]
                    if gitems:
                        # Check if group name already exists
                        existing = next((g for g in ingredient_groups if g["name"] == gname), None)
                        if existing:
                            for gi in gitems:
                                if gi not in existing["items"]:
                                    existing["items"].append(gi)
                        else:
                            ingredient_groups.append({"name": gname, "items": list(gitems)})

                # Merge steps. Some extractions have no "steps" list: the procedure is a
                # single "instructions_text" string, or embedded in a raw "text" transcript
                # under a "PROCEDIMIENTO" heading.
                item_steps = it.get("steps") or []
                if not item_steps and it.get("instructions_text"):
                    item_steps = [it["instructions_text"]]
                if not item_steps and it.get("text"):
                    m = re.search(r"procedimiento\s*:?\s*\n(.*)", it["text"], re.I | re.S)
                    if m:
                        item_steps = [m.group(1).strip()]
                for st in item_steps:
                    if st.strip() and st.strip() not in steps:
                        steps.append(st.strip())

                # Merge handwritten notes -> teacher_notes
                for hw in it.get("handwritten_notes", []):
                    if hw.strip() and hw.strip() not in teacher_notes:
                        teacher_notes.append(hw.strip())

                # Merge printed notes -> notes. Some extractions give a single string
                # instead of a list; iterating a raw string would shred it into characters.
                item_notes = it.get("notes") or []
                if isinstance(item_notes, str):
                    item_notes = [item_notes]
                for n in item_notes:
                    if n.strip() and n.strip() not in notes:
                        notes.append(n.strip())

            # Text string for classification
            ing_text = " ".join(ing for grp in ingredient_groups for ing in grp["items"])
            steps_text = " ".join(steps)

            category, tags = classify_recipe(title, ing_text, steps_text)

            recipe_data = {
                "title": title or "Receta sin título",
                "category": category,
                "tags": tags,
                "servings": servings,
                "prep_time": prep_time,
                "cook_time": cook_time,
                "temperature": temperature,
                "ingredient_groups": ingredient_groups,
                "steps": steps,
                "teacher_notes": teacher_notes,
                "notes": notes
            }

            rec_obj = {
                "cluster": cid,
                "kind": "recipe",
                "source_refs": refs,
                "source_hash": "verbatim_clean_v1",
                "recipe": recipe_data
            }

        # Write recipe file
        out_filename = f"{cid.replace('#', '_')}.json"
        out_path = Path("cache/recipes") / out_filename
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(rec_obj, f, indent=2, ensure_ascii=False)
        built_count += 1

    print(f"Successfully wrote {built_count} clean consolidated recipe files into cache/recipes/")

if __name__ == "__main__":
    main()
