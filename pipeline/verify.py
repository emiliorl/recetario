"""Check every consolidated recipe against the page extractions it came from (no API calls).

Consolidation rewrites the text, and a model (or a hand-written batch) can drift from it:
invent ingredients, change quantities, oven temperatures or times, add steps the page never had.
This compares cache/recipes/ with cache/pages/ word by word and number by number, and lists
anything it can't find in the source in cache/review.md.

Errors: an ingredient, quantity, temperature or time that isn't on the page, or a page ingredient
that's missing from the recipe. Warnings: steps, notes and paragraphs made mostly of words the
page doesn't use (often harmless rewording, sometimes invented technique).
To accept a finding after checking the scan, list the recipe id under `verified:` in data/overrides.yaml.
"""

import re
import unicodedata
from dataclasses import dataclass, field
from fractions import Fraction

from .cluster import load_overrides, ref
from .config import CLUSTERS_FILE
from .consolidate import cache_file
from .extract import cache_path
from .pages import list_pages
from .store import read_json, write_review_section

# Page fields that are the model's own labels, not text from the scan.
_SKIP_KEYS = {"kind", "normalized_title", "is_continuation", "category_hint", "index"}
_INGREDIENT_KEYS = {"ingredient_groups", "ingredients"}

# Units, connectors and filler that don't identify an ingredient.
_STOPWORDS = {
    "taza", "tazas", "tz", "cucharada", "cucharadas", "cda", "cdas", "cucharadita", "cucharaditas",
    "cucharita", "cucharitas", "cdta", "cdtas", "onza", "onzas", "oz", "libra", "libras", "lb", "gramos",
    "kilo", "litro", "litros", "pizca", "para", "con", "del", "las", "los", "una", "uno", "unos", "unas",
    "gusto", "aprox", "aproximadamente", "bien", "muy", "poco", "poquito", "cada", "partes", "parte",
    "opcional", "cortado", "cortada", "cortados", "cortadas", "picado", "picada", "picados", "picadas",
}

# Cooking verbs and filler a faithful rewrite may add without changing the recipe. Steps and notes
# are judged on the rest: ingredients, equipment and technique.
_GENERIC = """
agregar agregando anadir incorporar incorporando unir mezclar mezclando batir batiendo revolver
remover colocar poner dejar retirar pasar llevar verter echar servir hasta que este esten quede
queden durante mientras luego despues antes final finalmente aparte separado todo toda todos
medio media fuego lento alto bajo velocidad minuto minutos hora horas vez veces cuidado
suave suavemente completamente completo por forma manera movimientos envolventes envolvente
obtener lograr textura consistencia deseada homogenea homogeneo integrar integrado caliente frio
tibio enfriar precalentar horno molde tazon bowl recipiente olla sarten preparacion mezcla
""".split()

# Thresholds (share of an item's words found in the source).
INGREDIENT_MATCH = 0.5
TEXT_MATCH = 0.5
MIN_WORDS_TO_JUDGE = 3

_UNICODE_FRACTIONS = {"½": " 1/2", "¼": " 1/4", "¾": " 3/4", "⅓": " 1/3", "⅔": " 2/3", "⅛": " 1/8"}
_NUMBER = re.compile(r"\d+/\d+|\d+(?:[.,]\d+)?")
_NUMBER_WORDS = {"un": "1", "una": "1", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4", "cinco": "5",
                 "seis": "6", "media": "1/2", "medio": "1/2"}
_NUMBER_WORD = re.compile(r"\b(" + "|".join(_NUMBER_WORDS) + r")\b")
_PAGE_REF = re.compile(r"\bpags?\.?\s*\d+(?:\s*(?:,|y|-)\s*\d+)*")
_TIME_TOKEN = re.compile(
    r"(\d+(?: \d+/\d+)?|\d+/\d+)\s*(h|hrs?|horas?|min|mins|minutos?)?\b"  # amount, optional unit
    r"|\b(a|o|y)\b|[-–]"  # range or compound joiner
    r"|[a-zñ]+"  # any other word ends the phrase
)


def _plain(text: str) -> str:
    for char, repl in _UNICODE_FRACTIONS.items():
        text = text.replace(char, repl)
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


_SUFFIXES = sorted("""
amente mente iendo ando aron ieron ados adas idos idas ado ada ido ida ar er ir an en as es os a e o s
""".split(), key=len, reverse=True)


def _stem(word: str) -> str:
    """Crude Spanish stem so picada/picados, cebolla/cebollas and hornear/hornean compare equal."""
    for suffix in _SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def words(text: str) -> set[str]:
    return {_stem(w) for w in re.findall(r"[a-zñ]{3,}", _plain(text)) if w not in _STOPWORDS}


_GENERIC_STEMS = {_stem(w) for w in _GENERIC}


def _without_parentheses(text: str) -> str:
    return re.sub(r"\([^)]*\)", " ", text)


def numbers(text: str, spelled: bool = False) -> set[str]:
    """Numbers in the text, page references left out; spelled=True also reads "una"/"media" (for quantities)."""
    text = _PAGE_REF.sub("", _plain(text))
    if spelled:
        text = _NUMBER_WORD.sub(lambda m: _NUMBER_WORDS[m.group(1)], text)
    return {n.replace(",", ".") for n in _NUMBER.findall(text)}


def _amount(text: str) -> float:
    total = 0.0
    for part in text.split():
        top, _, bottom = part.partition("/")
        total += int(top) / int(bottom) if bottom else float(top)
    return total


def minutes(text: str) -> set[int]:
    """Every duration in the text, in minutes: "1 h 30 min a 2 h" -> {90, 120}, "40 a 45 minutos" -> {40, 45}."""
    found: set[int] = set()
    pending: list[float] = []  # amounts waiting for a unit, as in "40 a 45 minutos"
    hours = None  # "1 h" waiting for a possible "30 min"
    for match in _TIME_TOKEN.finditer(_plain(text)):
        value, unit, joiner = match.groups()
        if value and unit:
            scale = 60 if unit.startswith("h") else 1
            amount = round(_amount(value) * scale)
            found |= {round(p * scale) for p in pending}
            pending = []
            if hours is not None and scale == 1:
                found.add(hours + amount)
                hours = None
                continue
            if hours is not None:
                found.add(hours)
            hours = amount if scale == 60 else None
            if scale == 1:
                found.add(amount)
            continue
        if hours is not None and joiner != "y":
            found.add(hours)
            hours = None
        if value:
            pending.append(_amount(value))
        elif not joiner and match.group(0) not in "-–":
            pending = []  # a plain word: "2 tazas ... 25 minutos" is not a range
    if hours is not None:
        found.add(hours)
    return found


def _fraction(amount) -> str:
    if not isinstance(amount, (int, float)) or not amount:
        return ""
    whole, part = divmod(Fraction(amount).limit_denominator(8), 1)
    return " ".join(filter(None, [str(whole) if whole else "", str(part) if part else ""]))


def _strings(value, key: str = "", ingredient: bool = False):
    """Yield (text, is_ingredient_line) for every string in a page item."""
    if key in _SKIP_KEYS:
        return
    ingredient = ingredient or key in _INGREDIENT_KEYS
    if isinstance(value, str):
        if key not in ("name", "group"):
            yield value, ingredient
    elif isinstance(value, dict) and "name" in value and ("amount" in value or "unit" in value):
        # Structured ingredient: {"name": "azúcar", "amount": 1.5, "unit": "tazas"} -> "1 1/2 tazas azúcar".
        yield " ".join(filter(None, [_fraction(value.get("amount")), value.get("unit"), value["name"]])), True
    elif isinstance(value, dict):
        for k, v in value.items():
            yield from _strings(v, k, ingredient)
    elif isinstance(value, list):
        for v in value:
            yield from _strings(v, key, ingredient)


def _typed_ingredients(text: str) -> list[str]:
    """Ingredient lines of a page transcribed as plain text (INGREDIENTES: ... PROCEDIMIENTO:)."""
    match = re.search(r"ingredientes?:?\s*\n(.*?)(?:\n\s*(?:procedimiento|preparaci[oó]n|decoraci[oó]n)\b|\Z)",
                      text, re.I | re.S)
    if not match:
        return []
    # Sub-headings ("Salsa:", "DECORACION:") aren't ingredients.
    return [line.strip() for line in match.group(1).splitlines() if line.strip() and not line.strip().endswith(":")]


@dataclass
class Source:
    lines: list[str] = field(default_factory=list)
    ingredients: list[str] = field(default_factory=list)

    def add(self, item: dict) -> None:
        for text, is_ingredient in _strings(item):
            self.lines.append(text)
            if is_ingredient:
                self.ingredients.append(text)
            else:
                self.ingredients += _typed_ingredients(text)

    @property
    def text(self) -> str:
        return "\n".join(self.lines)


def _fahrenheit_to_celsius(values: set[str]) -> set[str]:
    """Allow a °C conversion of any oven temperature on the page, rounded however the writer liked."""
    allowed = set()
    for value in values:
        if "/" in value or float(value) < 200:
            continue
        celsius = (float(value) - 32) * 5 / 9
        allowed |= {str(c) for c in range(int(celsius) - 6, int(celsius) + 7)}
    return allowed


def _overlap(a: str, b: str) -> float:
    """Share of the shorter text's words that the other one has, parentheses included or not."""
    best = 0.0
    for x, y in ((a, b), (_without_parentheses(a), _without_parentheses(b))):
        wx, wy = words(x), words(y)
        if wx and wy:
            best = max(best, len(wx & wy) / min(len(wx), len(wy)))
    return best


def _matching_lines(item: str, lines: list[str]) -> list[str]:
    """Page lines that name the same ingredient, best match first."""
    scored = sorted(((_overlap(item, line), line) for line in lines), key=lambda s: -s[0])
    return [line for score, line in scored if score >= INGREDIENT_MATCH]


def check_recipe(recipe: dict, source: Source) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    source_words = words(source.text)
    source_numbers = numbers(source.text)
    allowed_numbers = source_numbers | _fahrenheit_to_celsius(source_numbers)
    source_minutes = minutes(source.text)

    items = [i for g in recipe.get("ingredient_groups") or [] for i in g.get("items") or []]
    lines = source.ingredients or source.lines
    for item in items:
        candidates = _matching_lines(item, lines) or _matching_lines(item, source.lines)
        if not candidates:
            errors.append(f"Ingrediente que no está en la página: «{item}»")
            continue
        # Against the matching page lines, not the whole page: "2 tazas" must not pass because a 2 appears
        # elsewhere. Several lines can match when the recipe merges versions; one agreeing is enough.
        # Numbers in parentheses are conversions or remarks ("(8 oz)"); they only need to be somewhere on the page.
        quantity = numbers(_without_parentheses(item), spelled=True)
        if not any(quantity <= numbers(line, spelled=True) | _fahrenheit_to_celsius(numbers(line)) for line in candidates):
            errors.append(f"Cantidad que no coincide con la página: «{item}» (página: «{candidates[0].strip()}»)")
        elif numbers(item) - numbers(_without_parentheses(item)) - allowed_numbers:
            errors.append(f"Cifra entre paréntesis que no está en la página: «{item}»")

    for line in source.ingredients:
        if words(line) and not any(_overlap(item, line) >= INGREDIENT_MATCH for item in items):
            errors.append(f"Falta un ingrediente de la página: «{line.strip()}»")

    temperature = recipe.get("temperature") or ""
    extra = numbers(temperature) - allowed_numbers
    if extra:
        errors.append(f"Temperatura que no está en la página: «{temperature}»")

    for key, label in (("prep_time", "Preparación"), ("cook_time", "Cocción")):
        value = recipe.get(key) or ""
        extra = minutes(value) - source_minutes
        if extra or (value and not minutes(value) and numbers(value) - source_numbers):
            errors.append(f"{label} que no está en la página: «{value}»")

    servings = recipe.get("servings") or ""
    if numbers(servings) - source_numbers:
        errors.append(f"Porciones que no están en la página: «{servings}»")

    for kind, texts in (("Paso", recipe.get("steps") or []), ("Nota", (recipe.get("notes") or []) + (recipe.get("teacher_notes") or []))):
        for text in texts:
            extra = numbers(text) - allowed_numbers
            if extra:
                errors.append(f"{kind} con cifras que no están en la página ({', '.join(sorted(extra))}): «{text}»")
            _check_text(kind, text, source_words, warnings)
    return errors, warnings


_LIST_MARKER = re.compile(r"^\s*(?:#+\s*)?\d+[.)]\s", re.M)  # "1. ", "### 2. ": numbering, not data


def check_tip(tip: dict, source: Source) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    source_words = words(source.text)
    allowed = numbers(source.text) | _fahrenheit_to_celsius(numbers(source.text))
    for text in tip.get("body") or []:
        for paragraph in re.split(r"\n\s*\n|\n(?=\s*(?:[-*]|\d+\.)\s)", text):
            extra = numbers(_LIST_MARKER.sub("", paragraph)) - allowed
            if extra:
                errors.append(f"Cifras que no están en la página ({', '.join(sorted(extra))}): «{_short(paragraph)}»")
            _check_text("Párrafo", paragraph, source_words, warnings)
    return errors, warnings


def _check_text(kind: str, text: str, source_words: set[str], warnings: list[str]) -> None:
    text_words = words(text) - _GENERIC_STEMS
    if len(text_words) < MIN_WORDS_TO_JUDGE:
        return
    found = len(text_words & source_words) / len(text_words)
    if found < TEXT_MATCH:
        unknown = ", ".join(sorted(text_words - source_words)[:8])
        warnings.append(f"{kind} con poco respaldo ({found:.0%}; no aparece: {unknown}): «{_short(text)}»")


def _short(text: str, limit: int = 140) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def run() -> list[str]:
    """Write the report; return the ids of recipes with errors."""
    clusters = read_json(CLUSTERS_FILE)
    pages_by_label = {p.label: p for p in list_pages()}
    verified = {ref(v) for v in load_overrides().get("verified") or []}

    report, failing, warned, checked = [], [], 0, 0
    for cluster in clusters:
        path = cache_file(cluster)
        if not path.exists() or cluster["id"] in verified:
            continue
        data = read_json(path)
        source = Source()
        for item_ref in cluster["refs"]:
            label, index = item_ref.split("#")
            source.add(read_json(cache_path(pages_by_label[label]))["items"][int(index) - 1])
        body = data[data["kind"]]
        check = check_recipe if data["kind"] == "recipe" else check_tip
        errors, warnings = check(body, source)
        checked += 1
        if not errors and not warnings:
            continue
        if errors:
            failing.append(cluster["id"])
        warned += bool(warnings)
        report.append(f"### {cluster['id']} · {body['title']} (páginas {', '.join(cluster['pages'])})")
        report.append("")
        report += [f"- ❌ {e}" for e in errors]
        if warnings:
            report += ["", f"<details><summary>⚠️ {len(warnings)} avisos</summary>", ""]
            report += [f"- {w}" for w in warnings] + ["", "</details>"]
        report.append("")

    summary = (
        f"{checked} revisadas: {len(failing)} con errores, {warned} con avisos. "
        "Corrige en cache/recipes/ (o vuelve a consolidar) y, si el escaneo confirma que está bien, "
        "agrega el id a `verified:` en data/overrides.yaml."
    )
    write_review_section("Verificación contra la fuente", [summary, ""] + report)
    print(summary)
    for cluster_id in failing:
        print(f"  ❌ {cluster_id}")
    return failing
