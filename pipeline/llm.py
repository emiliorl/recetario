"""Provider adapter. Every model call goes through this module, so switching
providers means reimplementing the three public functions below."""

import base64
import io
import json
from functools import cache
from pathlib import Path

from PIL import Image, ImageOps

from .config import CATEGORIES, CONSOLIDATE_MODEL, EXTRACT_MODEL, IMAGE_MAX_EDGE, TAGS
from .schemas import PageExtraction, Recipe, Tip

EXTRACT_PROMPT = """Esta imagen es una página escaneada de un recetario familiar en español (carpeta de clases de cocina).

Transcribe la página a la estructura pedida:
- Una página puede tener varias recetas o consejos: crea un elemento en items por cada uno, en orden de arriba abajo.
- Copia el texto exactamente como está escrito, en español. No traduzcas, no corrijas cantidades ni ortografía.
- Separa ingredientes (uno por línea, con su cantidad) de los pasos del procedimiento.
- Las notas escritas a mano, correcciones al margen o consejos de la maestra van en handwritten_notes del elemento al que acompañan.
- Si la página empieza a mitad de una receta (sin título, a mitad de una lista o de un paso), el primer elemento tiene is_continuation true.
- Si el último elemento se corta y sigue en otra página, continues_next es true.
- Ignora los encabezados repetidos (nombre del instituto, curso, catedrática, "Edith's Kitchen") y los dibujos.
- Usa cadena vacía o lista vacía para lo que no aparezca."""

RECIPE_PROMPT = """Abajo están las transcripciones (JSON) de uno o varios fragmentos de un recetario que corresponden a la MISMA receta:
partes de una receta partida en varias páginas, o versiones duplicadas (el apunte original de la maestra y una copia pasada en limpio).

Une todo en una sola receta coherente, en español:
- Conserva el orden lógico: si hay fragmentos, junta ingredientes y pasos en el orden correcto.
- Si hay versiones duplicadas, usa la redacción más clara como base, pero no pierdas ningún dato práctico (cantidades, temperaturas, tiempos).
- Todas las notas a mano y consejos de la maestra van en teacher_notes; no descartes ninguna. No incluyas créditos del curso (cátedra, instituto, nombre de la profesora).
- No inventes cantidades, pasos ni tiempos que no estén en las páginas. Deja vacío lo que no aparezca.
- Corrige solo errores evidentes de transcripción (letras cambiadas), no el contenido.
- Elige UNA categoría: {categories}.
- Elige de 0 a 4 etiquetas de esta lista, solo si aplican claramente: {tags}.

Fragmentos:
{pages}"""

TIP_PROMPT = """Abajo están las transcripciones (JSON) de uno o varios fragmentos de un recetario que contienen un consejo de cocina,
una tabla de equivalencias o una guía (no una receta). Redáctalo como un artículo breve en español, en Markdown:
cada elemento de body es un párrafo, una lista o una tabla Markdown. Conserva todo el contenido y no inventes nada.

Fragmentos:
{pages}"""

# Refused requests are re-run server-side on Anthropic's recommended fallback model.
FALLBACK_HEADERS = {"anthropic-beta": "server-side-fallback-2026-07-01"}
FALLBACK_BODY = {"fallbacks": "default"}


class ModelError(RuntimeError):
    pass


@cache
def _client():
    import anthropic
    from dotenv import load_dotenv

    load_dotenv()
    return anthropic.Anthropic(max_retries=5)


def _encode_image(path: Path) -> str:
    with Image.open(path) as img:
        img = ImageOps.exif_transpose(img).convert("RGB")
        img.thumbnail((IMAGE_MAX_EDGE, IMAGE_MAX_EDGE))
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=88)
    return base64.standard_b64encode(buf.getvalue()).decode("ascii")


def _parse(model, schema, content, max_tokens=16000, fallbacks=False):
    kwargs = {}
    if fallbacks:
        kwargs = {"extra_headers": FALLBACK_HEADERS, "extra_body": FALLBACK_BODY}
    response = _client().messages.parse(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": content}],
        output_format=schema,
        **kwargs,
    )
    if response.stop_reason == "refusal":
        raise ModelError(f"refused: {response.stop_details}")
    if response.stop_reason == "max_tokens":
        raise ModelError("output truncated (max_tokens)")
    if response.parsed_output is None:
        raise ModelError("no parsed output")
    return response.parsed_output, response.usage


def extract_page(path: Path):
    """Pass 1: one scanned page -> PageExtraction."""
    content = [
        {
            "type": "image",
            "source": {"type": "base64", "media_type": "image/jpeg", "data": _encode_image(path)},
        },
        {"type": "text", "text": EXTRACT_PROMPT},
    ]
    return _parse(EXTRACT_MODEL, PageExtraction, content, fallbacks=True)


def _parts_json(parts: dict[str, dict]) -> str:
    return "\n\n".join(
        f"--- {name} ---\n{json.dumps(data, ensure_ascii=False, indent=1)}" for name, data in parts.items()
    )


def consolidate_recipe(parts: dict[str, dict]):
    """Pass 2: the page items of one cluster, keyed by a readable name -> Recipe."""
    prompt = RECIPE_PROMPT.format(
        categories=", ".join(CATEGORIES.values()),
        tags=", ".join(TAGS),
        pages=_parts_json(parts),
    )
    return _parse(CONSOLIDATE_MODEL, Recipe, prompt, max_tokens=8000)


def consolidate_tip(parts: dict[str, dict]):
    """Pass 2: the page items of one tip cluster -> Tip."""
    return _parse(CONSOLIDATE_MODEL, Tip, TIP_PROMPT.format(pages=_parts_json(parts)), max_tokens=8000)
