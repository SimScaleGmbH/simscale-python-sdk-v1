from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class IntegerToDimensionalScalarValueConversion(SimScaleModel):
    integer_value: Any | None = Field(
        validation_alias="integerValue",
        serialization_alias="integerValue",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    unit: Any | None = Field(
        default=None, description="Value model for a measurement unit value. Resolves to a text JSON node."
    )
    value_model_type: str
