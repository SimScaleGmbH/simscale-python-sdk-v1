from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DimensionalScalarFunctionPow(SimScaleModel):
    argument1: Any | None = Field(
        default=None,
        description="Value model for a dimensional scalar.  Resolves to an object node with field `value` (double node) and field `unit` (text node).  Note: during resolution dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s), unless the resolution context opts out of the conversion to keep the original units; results of operations are always in base SI units.",
    )
    argument2: Any | None = Field(
        default=None, description="Value model for a 64-bit signed integer value. Resolves to a long JSON node."
    )
    value_model_type: str
