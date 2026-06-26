from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EnumValueLabel(SimScaleModel):
    """Label information for one particular enum value."""

    label: str | None = Field(default=None)
    multi_language_label: dict[str, str] | None = Field(
        validation_alias="multiLanguageLabel", serialization_alias="multiLanguageLabel", default=None
    )
