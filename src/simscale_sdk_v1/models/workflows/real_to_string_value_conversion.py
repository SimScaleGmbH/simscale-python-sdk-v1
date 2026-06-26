from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RealToStringValueConversion(SimScaleModel):
    real_value: Any | None = Field(
        validation_alias="realValue",
        serialization_alias="realValue",
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
    value_model_type: str
