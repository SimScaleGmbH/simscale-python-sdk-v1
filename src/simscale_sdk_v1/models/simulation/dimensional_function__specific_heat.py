from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_heat_value import (
    OneOf_DimensionalFunction_SpecificHeatValue,
)


class DimensionalFunction_SpecificHeat(SimScaleModel):
    value: OneOf_DimensionalFunction_SpecificHeatValue | None = Field(default=None)
    unit: Literal["J/(kg·K)", "Btu/(lb·°F)"]
