"""Read what a page extraction says, in a form that can be compared: plain words and numbers.

Page files come in several shapes (ingredient groups, flat ingredient lists, structured amounts,
plain typed text), so everything goes through Source, which keeps every line and picks out the
ingredient lines. Used by cluster (is this the same recipe?) and verify (does the recipe match?).
"""

import re
import unicodedata
from dataclasses import dataclass, field
from fractions import Fraction

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

_UNICODE_FRACTIONS = {"½": " 1/2", "¼": " 1/4", "¾": " 3/4", "⅓": " 1/3", "⅔": " 2/3", "⅛": " 1/8"}
_NUMBER = re.compile(r"\d+/\d+|\d+(?:[.,]\d+)?")
_NUMBER_WORDS = {"un": "1", "una": "1", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4", "cinco": "5",
                 "seis": "6", "media": "1/2", "medio": "1/2"}
_NUMBER_WORD = re.compile(r"\b(" + "|".join(_NUMBER_WORDS) + r")\b")
_PAGE_REF = re.compile(r"\bpags?\.?\s*\d+(?:\s*(?:,|y|-)\s*\d+)*")

def plain(text: str) -> str:
    for char, repl in _UNICODE_FRACTIONS.items():
        text = text.replace(char, repl)
    text = unicodedata.normalize("NFD", text.lower())
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


_SUFFIXES = sorted("""
amente mente iendo ando aron ieron ados adas idos idas ado ada ido ida ar er ir an en as es os a e o s
""".split(), key=len, reverse=True)


def stem(word: str) -> str:
    """Crude Spanish stem so picada/picados, cebolla/cebollas and hornear/hornean compare equal."""
    for suffix in _SUFFIXES:
        if word.endswith(suffix) and len(word) - len(suffix) >= 4:
            return word[: -len(suffix)]
    return word


def words(text: str) -> set[str]:
    return {stem(w) for w in re.findall(r"[a-zñ]{3,}", plain(text)) if w not in _STOPWORDS}


def without_parentheses(text: str) -> str:
    return re.sub(r"\([^)]*\)", " ", text)


def numbers(text: str, spelled: bool = False) -> set[str]:
    """Numbers in the text, page references left out; spelled=True also reads "una"/"media" (for quantities)."""
    text = _PAGE_REF.sub("", plain(text))
    if spelled:
        text = _NUMBER_WORD.sub(lambda m: _NUMBER_WORDS[m.group(1)], text)
    return {n.replace(",", ".") for n in _NUMBER.findall(text)}


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


def overlap(a: str, b: str) -> float:
    """Share of the shorter text's words that the other one has, parentheses included or not."""
    best = 0.0
    for x, y in ((a, b), (without_parentheses(a), without_parentheses(b))):
        wx, wy = words(x), words(y)
        if wx and wy:
            best = max(best, len(wx & wy) / min(len(wx), len(wy)))
    return best


def _ingredient_key(line: str) -> tuple[set[str], set[str]]:
    """What identifies an ingredient line: its words and its quantity (remarks in parentheses left out)."""
    main = without_parentheses(line)
    return words(main) or words(line), numbers(main, spelled=True)


def shared_ingredients(a: Source, b: Source) -> float | None:
    """Share of both ingredient lists that the other has with the same quantity; None if either has none.

    Two copies of one recipe score 0.8-1.0 (transcription differences aside). Different recipes that
    happen to share a title, or staples like harina and azúcar, score well under 0.4, because the
    quantities differ.
    """
    keys_a = [k for k in map(_ingredient_key, a.ingredients) if k[0]]
    keys_b = [k for k in map(_ingredient_key, b.ingredients) if k[0]]
    if not keys_a or not keys_b:
        return None

    def found(key, others) -> bool:
        return any(key[1] == o[1] and len(key[0] & o[0]) / min(len(key[0]), len(o[0])) >= 0.6 for o in others)

    matched = sum(found(k, keys_b) for k in keys_a) + sum(found(k, keys_a) for k in keys_b)
    return matched / (len(keys_a) + len(keys_b))
