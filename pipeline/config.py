"""Paths, model settings and the recipe taxonomy."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PICTURES_DIR = ROOT / "pictures"
CACHE_DIR = ROOT / "cache"
PAGES_CACHE = CACHE_DIR / "pages"
RECIPES_CACHE = CACHE_DIR / "recipes"
CLUSTERS_FILE = CACHE_DIR / "clusters.json"
REVIEW_FILE = CACHE_DIR / "review.md"
OVERRIDES_FILE = ROOT / "data" / "overrides.yaml"
SITE_DIR = ROOT / "site"
VAULT_DIR = ROOT / "vault"  # encrypted copy of cache/, the only form committed to Git

# Pass 1 (vision) and pass 2 (text-only consolidation).
EXTRACT_MODEL = "claude-opus-5"
CONSOLIDATE_MODEL = "claude-haiku-4-5"
EXTRACT_WORKERS = 4
CONSOLIDATE_WORKERS = 4
IMAGE_MAX_EDGE = 1568

# Title similarity (rapidfuzz token_set_ratio, 0-100).
AUTO_MERGE_SCORE = 92
REVIEW_MERGE_SCORE = 80

# Folder slug -> display name. Order is the sidebar order.
CATEGORIES = {
    "panes-y-masas": "Panes y masas",
    "postres-y-pasteles": "Postres y pasteles",
    "platos-principales": "Platos principales",
    "sopas-y-cremas": "Sopas y cremas",
    "entradas-y-bocadillos": "Entradas y bocadillos",
    "salsas-y-aderezos": "Salsas y aderezos",
    "basicos-y-rellenos": "Básicos y rellenos",
    "bebidas": "Bebidas",
}

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

# Render-only cleanup of tags the model wrote in other words (older runs used a looser list).
TAG_ALIASES = {
    "al horno": "horneado",
    "fiestas": "festivo",
    "pescados y mariscos": "pescado y mariscos",
}

# Which consejos to suggest on which recipes. Key: words from the consejo's title.
# "title": words looked for in the recipe title (whole words, plurals included).
# "body": in its ingredients and steps, so only unambiguous words here: "glass" there is almost
# always azúcar glass, "fondo" the bottom of the pan, "pasta" a dough.
# "skip": categories never linked, e.g. dessert sauces are not the savory sauce technique.
# A title match counts more than a body match; the best MAX_TIPS_PER_RECIPE are shown.
SAVORY_ONLY = ["Postres y pasteles", "Bebidas"]
TIP_LINKS = {
    "usos del glass": {"title": ["glass", "decorado", "decorar"]},
    "cartuchos": {"title": ["glass", "decorado", "decorar"], "body": ["cartucho", "manga pastelera"]},
    "aperitivos": {"title": ["canape", "dip", "bola de queso", "rollito", "pate", "camembert", "tostada"]},
    "sopas": {"title": ["sopa", "consome", "caldo"], "body": ["roux"]},
    "familias de salsas": {"title": ["salsa", "mayonesa"], "body": ["bechamel", "holandesa"], "skip": SAVORY_ONLY},
    "maridaje de salsas": {"title": ["salsa"], "skip": SAVORY_ONLY},
    "salsas a base de roux": {"body": ["roux", "bechamel", "salsa blanca"], "skip": SAVORY_ONLY},
    "huevos": {"title": ["huevo", "quiche", "omelette", "frijol", "lenteja", "garbanzo"]},
    "pastas y arroz": {"title": ["arroz", "espagueti", "noquis", "lasana", "tallarin", "macarron", "canelon"]},
    "ensaladas": {"title": ["ensalada", "aderezo", "vinagreta"], "body": ["vinagreta"]},
    "verduras": {"title": ["souffle", "verdura", "coliflor", "esparrago", "zucchini", "brocoli", "papa", "pure"]},
    "asar": {
        "title": ["pescado", "robalo", "atun", "corvina", "camaron", "filete", "barbacoa", "a la parrilla"],
        "body": ["parrilla", "a la plancha"],
    },
    "tabla de asados": {"title": ["roast beef", "asado", "pavo", "pierna", "lomo", "lomito", "jamon virginia"]},
    "cortes de carne": {
        "title": ["roast beef", "lomo", "lomito", "medallon", "carne", "costilla", "solomillo", "punta de"],
        "skip": SAVORY_ONLY,
    },
    "estofar": {"title": ["pollo", "pechuga", "pavo", "alita", "estofado", "guiso"], "body": ["estofar"]},
    # Not a bare "relleno": "Relleno de cocoa" is a cake filling.
    "saltear": {
        "title": ["rellenos", "rellena", "con relleno", "relleno tradicional", "salteado"],
        "body": ["saltear"],
        "skip": SAVORY_ONLY,
    },
}
MAX_TIPS_PER_RECIPE = 3

# How the home page groups tags in the filter panel. Tags not listed go under "Otras".
TAG_GROUPS = {
    "Ocasión": ["rápido", "fácil", "económico", "desayuno", "festivo", "congelable"],
    "Sabor": ["dulce", "salado", "chocolate", "frutas"],
    "Técnica": ["horneado", "sin horno", "frito", "guiso", "baño maría", "levadura"],
    "Ingrediente": ["vegetariano", "carne", "pollo", "pescado y mariscos", "pasta"],
}
