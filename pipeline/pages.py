"""Map scan files ("recetario _N.jpg", "recetario _N_K.jpg") to page labels without renaming them.

"recetario _157.jpg" -> label "157"; "recetario _157_1.jpg" -> label "157-1", sorted right after 157.
"""

import re
from dataclasses import dataclass
from functools import cache
from pathlib import Path

from .config import PICTURES_DIR

_NUMBER = re.compile(r"_(\d+)(?:_(\d+))?$")


@dataclass(frozen=True)
class Page:
    number: int
    sub: int
    path: Path

    @property
    def label(self) -> str:
        return f"{self.number}-{self.sub}" if self.sub else str(self.number)

    @property
    def id(self) -> str:
        return f"page_{self.number:03d}" + (f"_{self.sub}" if self.sub else "")


@cache
def list_pages() -> tuple[Page, ...]:
    pages = []
    for path in PICTURES_DIR.glob("*.jpg"):
        match = _NUMBER.search(path.stem.replace(" ", ""))
        if not match:
            raise ValueError(f"No page number in filename: {path.name}")
        pages.append(Page(int(match.group(1)), int(match.group(2) or 0), path))
    pages.sort(key=lambda p: (p.number, p.sub))
    return tuple(pages)


def page_order() -> dict[str, int]:
    """Label -> position in the binder, for detecting consecutive pages."""
    return {p.label: i for i, p in enumerate(list_pages())}


def parse_range(spec: str | None) -> set[int] | None:
    """'1-5,9,100' -> {1,2,3,4,5,9,100}. None means all pages."""
    if not spec:
        return None
    selected: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            lo, hi = part.split("-", 1)
            selected.update(range(int(lo), int(hi) + 1))
        elif part:
            selected.add(int(part))
    return selected


def select_pages(spec: str | None) -> list[Page]:
    """Pages whose number is in the range; '157' also selects '157-1'."""
    wanted = parse_range(spec)
    return [p for p in list_pages() if wanted is None or p.number in wanted]
