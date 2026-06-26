from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RealToIntegerConversion(SimScaleModel):
    argument: Any | None = Field(
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
    real_to_integer_conversion_type: Literal["ROUND", "CEIL", "FLOOR"] | None = Field(
        validation_alias="realToIntegerConversionType",
        serialization_alias="realToIntegerConversionType",
        default="",
        description="Real value conversion to integer value strategies.",
    )
    value_model_type: str
