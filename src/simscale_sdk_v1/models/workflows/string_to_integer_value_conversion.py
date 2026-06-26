from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StringToIntegerValueConversion(SimScaleModel):
    string_value: Any | None = Field(
        validation_alias="stringValue",
        serialization_alias="stringValue",
        default=None,
        description="Value model for a string value. Resolves to a text JSON node.",
    )
