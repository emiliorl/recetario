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
