from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EnumValueDoc(SimScaleModel):
    """Documentation for one particular enum value."""

    doc: str | None = Field(default=None)
    multi_language_doc: dict[str, str] | None = Field(
        validation_alias="multiLanguageDoc", serialization_alias="multiLanguageDoc", default=None
    )
