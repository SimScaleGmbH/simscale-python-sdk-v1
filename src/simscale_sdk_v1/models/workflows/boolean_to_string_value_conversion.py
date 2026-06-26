from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class BooleanToStringValueConversion(SimScaleModel):
    boolean_value: Any | None = Field(
        validation_alias="booleanValue",
        serialization_alias="booleanValue",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
    value_model_type: str
