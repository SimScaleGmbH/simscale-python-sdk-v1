from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__length_value import (
    OneOf_DimensionalVectorFunction_LengthValue,
)


class DimensionalVectorFunction_Length(SimScaleModel):
    value: OneOf_DimensionalVectorFunction_LengthValue | None = Field(default=None)
    unit: Literal["m", "in", "mm", "cm", "ft", "yd"]
