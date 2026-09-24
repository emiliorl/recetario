"""JSON checkpoints and the human review report."""

import json
import os
import re
from pathlib import Path

from .config import REVIEW_FILE


def write_json(path: Path, data) -> None:
    """Write atomically so an interrupted run never leaves a half-written checkpoint."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_review_section(name: str, lines: list[str]) -> None:
    """Replace one '## name' section of cache/review.md, keeping the others."""
    sections: dict[str, str] = {}
    if REVIEW_FILE.exists():
        text = REVIEW_FILE.read_text(encoding="utf-8")
        for match in re.finditer(r"^## (.+?)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
            sections[match.group(1).strip()] = match.group(2).strip()
    sections[name] = "\n".join(lines) if lines else "_Nada que revisar._"
    body = "\n\n".join(f"## {key}\n\n{value}" for key, value in sections.items())
    REVIEW_FILE.parent.mkdir(parents=True, exist_ok=True)
    REVIEW_FILE.write_text(f"# Revisión manual\n\n{body}\n", encoding="utf-8")
