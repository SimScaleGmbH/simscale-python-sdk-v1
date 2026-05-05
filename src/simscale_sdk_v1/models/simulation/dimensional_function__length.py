from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__length_value import (
    OneOf_DimensionalFunction_LengthValue,
)


class DimensionalFunction_Length(SimScaleModel):
    value: OneOf_DimensionalFunction_LengthValue | None = Field(default=None)
    unit: Literal["m", "in", "mm", "cm", "ft", "yd"]
