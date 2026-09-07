from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DimensionalScalarToStringValueConversion(SimScaleModel):
    dimensional_scalar_value: Any | None = Field(
        validation_alias="dimensionalScalarValue",
        serialization_alias="dimensionalScalarValue",
        default=None,
        description="Value model for a dimensional scalar.  Resolves to an object node with field `value` (double node) and field `unit` (text node).  Note: during resolution dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s), unless the resolution context opts out of the conversion to keep the original units; results of operations are always in base SI units.",
    )
    value_model_type: str
