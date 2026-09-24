"""Structured-output schemas for both model passes."""

from typing import Literal

from pydantic import BaseModel, Field

from .config import CATEGORIES, TAGS

Category = Literal[tuple(CATEGORIES.values())]  # type: ignore[valid-type]
Tag = Literal[tuple(TAGS)]  # type: ignore[valid-type]


class IngredientGroup(BaseModel):
    name: str = Field(description="Sub-heading such as 'Para la cubierta'; empty string if none.")
    items: list[str] = Field(description="One ingredient per entry, quantity included, as written.")


class PageItem(BaseModel):
    kind: Literal["recipe", "tip"] = Field(
        description="recipe, or tip for a cooking guide, conversion chart or standalone advice."
    )
    is_continuation: bool = Field(
        description=(
            "True only for the first item on the page when it continues a recipe from the previous "
            "page: it has no title of its own and starts mid-list or mid-step."
        )
    )
    title: str = Field(description="Title exactly as written; empty string if none.")
    normalized_title: str = Field(
        description="Title in lowercase without accents or punctuation, e.g. 'brazo gitano'; empty if none."
    )
    servings: str = Field(description="As written, or empty string.")
    prep_time: str = Field(description="As written, or empty string.")
    cook_time: str = Field(description="As written, or empty string.")
    temperature: str = Field(description="Oven temperature as written, or empty string.")
    ingredient_groups: list[IngredientGroup]
    steps: list[str] = Field(description="Procedure, one paragraph or numbered step per entry, verbatim.")
    notes: list[str] = Field(description="Printed notes, variations or serving suggestions.")
    handwritten_notes: list[str] = Field(
        description="Handwritten margin notes, corrections and teacher tips next to this item, verbatim."
    )


class PageExtraction(BaseModel):
    skip_reason: Literal["", "index", "cover", "blank", "other"] = Field(
        description="Empty string if the page has recipes or tips; otherwise why it has none."
    )
    items: list[PageItem] = Field(description="Every recipe or tip on the page, top to bottom.")
    continues_next: bool = Field(description="True if the last item is visibly cut off and continues on another page.")
    legibility: Literal["good", "partial", "poor"]
    rotation_issue: bool = Field(description="True if the page appears rotated or upside down.")


class Recipe(BaseModel):
    title: str = Field(description="Clean display title in Spanish, proper capitalization.")
    category: Category
    tags: list[Tag] = Field(description="0-4 tags that clearly apply.")
    servings: str
    prep_time: str
    cook_time: str
    temperature: str
    ingredient_groups: list[IngredientGroup]
    steps: list[str] = Field(description="Ordered steps, one action or short paragraph each.")
    teacher_notes: list[str] = Field(description="Handwritten margin notes and teacher secrets.")
    notes: list[str] = Field(description="Other printed notes, variations, serving suggestions.")


class Tip(BaseModel):
    title: str
    body: list[str] = Field(description="Paragraphs, lists or tables in Markdown, verbatim.")
