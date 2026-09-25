import json
import glob
from pathlib import Path

recipes_data = []

for path in sorted(glob.glob("cache/recipes/*.json")):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    cid = data.get("cluster", Path(path).stem)
    kind = data.get("kind", "recipe")
    
    if kind == "recipe":
        r = data.get("recipe", {})
        title = r.get("title", "Sin título")
        steps = r.get("steps", [])
        groups = r.get("ingredient_groups", [])
        items = [it for g in groups for it in g.get("items", [])]
        servings = r.get("servings", "").strip()
        prep_time = r.get("prep_time", "").strip()
        cook_time = r.get("cook_time", "").strip()
        temp = r.get("temperature", "").strip()
        notes = r.get("notes", [])
        teacher_notes = r.get("teacher_notes", [])
        
        issues = []
        if not steps:
            issues.append("Sin pasos de preparación")
        if not items:
            issues.append("Sin lista de ingredientes")
        if not servings:
            issues.append("Sin porciones especificadas")
        if not prep_time and not cook_time:
            issues.append("Sin tiempo de preparación ni cocción")
        if not temp and any(k in " ".join(steps).lower() for k in ["hornear", "horno", "grados", "350"]):
            issues.append("Menciona horno pero no temperatura")
            
        full_text = json.dumps(r, ensure_ascii=False).lower()
        fragment_markers = ["fragmento", "incomplet", "falta", "continuación sin", "cortad"]
        for marker in fragment_markers:
            if marker in full_text:
                issues.append(f"Mención textual de posible fragmento/incompleto: '{marker}'")
                break
                
        # Check for placeholders or question marks in ingredients or steps
        unknowns = []
        for it in items:
            if "?" in it or "[...]" in it or "[?]" in it:
                unknowns.append(f"Ingrediente dudoso: {it}")
        for s in steps:
            if "?" in s or "[...]" in s or "[?]" in s:
                unknowns.append(f"Paso con incógnitas: {s}")
                
        recipes_data.append({
            "id": cid,
            "title": title,
            "file": path,
            "steps_count": len(steps),
            "items_count": len(items),
            "servings": servings,
            "prep_time": prep_time,
            "cook_time": cook_time,
            "temperature": temp,
            "notes": notes,
            "teacher_notes": teacher_notes,
            "issues": issues,
            "unknowns": unknowns
        })

print(f"Total recipes evaluated: {len(recipes_data)}")

# 1. Structural incompleteness (missing steps, missing ingredients, or explicit fragments)
print("\n=== 1. RECETAS CON INFORMACIÓN ESTRUCTURALMENTE INCOMPLETA / FRAGMENTOS ===")
structural = [r for r in recipes_data if any("Sin pasos" in i or "Sin ingredientes" in i or "fragmento" in i for i in r["issues"])]
for r in structural:
    print(f"\n[{r['id']}] {r['title']} ({r['file']})")
    for i in r['issues']:
        print(f"  - {i}")
    if r['notes']:
        print(f"  Notas: {r['notes']}")

# 2. Recipes with unknowns/question marks
print("\n=== 2. RECETAS CON SIGNOS DE INTERROGACIÓN O DATOS ILEGIBLES ===")
with_unknowns = [r for r in recipes_data if r["unknowns"]]
for r in with_unknowns:
    print(f"\n[{r['id']}] {r['title']}")
    for u in r['unknowns']:
        print(f"  - {u}")

# 3. Missing metadata (times / servings / temperature)
print("\n=== 3. RECETAS CON METADATOS FALTANTES (RESUMEN) ===")
no_servings = [r for r in recipes_data if not r["servings"]]
no_times = [r for r in recipes_data if not r["prep_time"] and not r["cook_time"]]
no_temp = [r for r in recipes_data if "Menciona horno pero no temperatura" in r["issues"]]

print(f"- Sin porciones: {len(no_servings)} recetas")
print(f"- Sin tiempos (prep/cook): {len(no_times)} recetas")
print(f"- Con horneado pero sin temperatura en metadatos: {len(no_temp)} recetas")

if no_servings:
    print("\nEjemplos sin porciones:", [r['title'] for r in no_servings[:10]])
if no_times:
    print("Ejemplos sin tiempos:", [r['title'] for r in no_times[:10]])
if no_temp:
    print("Ejemplos sin temperatura:", [r['title'] for r in no_temp[:10]])
