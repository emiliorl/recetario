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

# How the home page groups tags in the filter panel. Tags not listed go under "Otras".
TAG_GROUPS = {
    "Ocasión": ["rápido", "fácil", "económico", "desayuno", "festivo", "congelable"],
    "Sabor": ["dulce", "salado", "chocolate", "frutas"],
    "Técnica": ["horneado", "sin horno", "frito", "guiso", "baño maría", "levadura"],
    "Ingrediente": ["vegetariano", "carne", "pollo", "pescado y mariscos", "pasta"],
}
