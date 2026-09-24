"""Step 1: sanity-check the scans before paying for any API calls."""

import hashlib
from statistics import median

from PIL import Image, ImageFilter, ImageStat

from .pages import list_pages
from .store import write_review_section

BLURRY_REPORT_COUNT = 10


def _sharpness(img: Image.Image) -> float:
    gray = img.convert("L")
    gray.thumbnail((1000, 1000))
    return ImageStat.Stat(gray.filter(ImageFilter.FIND_EDGES)).var[0]


def run() -> None:
    pages = list_pages()
    numbers = [p.number for p in pages]
    gaps = sorted(set(range(1, max(numbers) + 1)) - set(numbers))

    hashes: dict[str, list[int]] = {}
    rows = []
    for page in pages:
        hashes.setdefault(hashlib.sha256(page.path.read_bytes()).hexdigest(), []).append(page.number)
        with Image.open(page.path) as img:
            orientation = img.getexif().get(0x0112, 1)
            rows.append((page.number, img.size, orientation, _sharpness(img)))

    duplicates = [nums for nums in hashes.values() if len(nums) > 1]
    landscape = [n for n, (w, h), _, _ in rows if w > h]
    rotated = [n for n, _, orientation, _ in rows if orientation not in (1, None)]
    typical = median(s for *_, s in rows)
    blurry = sorted(rows, key=lambda r: r[3])[:BLURRY_REPORT_COUNT]

    lines = [
        f"- Páginas: {len(pages)} (de la {numbers[0]} a la {numbers[-1]})",
        f"- Números faltantes: {', '.join(map(str, gaps)) or 'ninguno'}",
        f"- Archivos idénticos: {'; '.join(map(str, duplicates)) or 'ninguno'}",
        f"- Páginas horizontales (¿giradas?): {', '.join(map(str, landscape)) or 'ninguna'}",
        f"- Con rotación EXIF: {', '.join(map(str, rotated)) or 'ninguna'}",
        "",
        f"Páginas menos nítidas (nitidez típica {typical:.0f}; revisar a ojo):",
        "",
    ]
    lines += [f"- página {n}: {s:.0f}" for n, _, _, s in blurry]
    write_review_section("Auditoría de escaneos", lines)
    print("\n".join(lines))
