from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EnumToStringValueConversion(SimScaleModel):
    enum_value: Any | None = Field(
        validation_alias="enumValue",
        serialization_alias="enumValue",
        default=None,
        description="Value model for an enum value. Resolves to a text JSON node.",
    )
    value_model_type: str
