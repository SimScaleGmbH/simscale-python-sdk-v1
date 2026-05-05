from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__density_value import (
    OneOf_DimensionalFunction_DensityValue,
)


class DimensionalFunction_Density(SimScaleModel):
    value: OneOf_DimensionalFunction_DensityValue | None = Field(default=None)
    unit: Literal["kg/m³", "lb/in³", "g/mm³", "g/cm³", "t/mm³", "lb/ft³"]
