"""Shrunk, encrypted copies of the scans, so the site can show the original page under each recipe.

scans/ is committed (the JPGs never are) and render copies it into the site. The browser decrypts
a scan with the family key only when someone opens "Ver página original" (see assets/app.js).
Needs pictures/, so it runs locally, not in GitHub Actions.
"""

import io

from PIL import Image, ImageOps

from . import crypto
from .config import SCAN_MAX_EDGE, SCAN_QUALITY, SCANS_DIR
from .pages import list_pages


def scan_name(label: str) -> str:
    """Opaque file name, so the site's file list doesn't reveal anything either."""
    return crypto.opaque_id(f"scan/{label}") + ".bin"


def _shrink(path) -> bytes:
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image).convert("RGB")
        image.thumbnail((SCAN_MAX_EDGE, SCAN_MAX_EDGE))
        out = io.BytesIO()
        image.save(out, "JPEG", quality=SCAN_QUALITY, optimize=True, progressive=True)
        return out.getvalue()


def run(force: bool = False) -> None:
    pages = list_pages()
    if not pages:
        raise SystemExit("No hay escaneos en pictures/: nada que publicar (scans/ se deja como está).")
    SCANS_DIR.mkdir(exist_ok=True)
    live, written = set(), 0
    for page in pages:
        name = scan_name(page.label)
        live.add(name)
        target = SCANS_DIR / name
        # A new password gives new names, so a stale copy is never kept by this check.
        if not force and target.exists() and target.stat().st_mtime >= page.path.stat().st_mtime:
            continue
        target.write_bytes(crypto.encrypt_asset(name, _shrink(page.path)))
        written += 1
    removed = 0
    for target in SCANS_DIR.glob("*.bin"):
        if target.name not in live:
            target.unlink()
            removed += 1
    size = sum(p.stat().st_size for p in SCANS_DIR.glob("*.bin")) / 1e6
    print(f"scans/: {written} escaneos cifrados, {removed} eliminados, {len(live)} en total ({size:.0f} MB)")
