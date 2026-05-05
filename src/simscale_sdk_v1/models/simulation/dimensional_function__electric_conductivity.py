from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_conductivity_value import (
    OneOf_DimensionalFunction_ElectricConductivityValue,
)


class DimensionalFunction_ElectricConductivity(SimScaleModel):
    value: OneOf_DimensionalFunction_ElectricConductivityValue | None = Field(default=None)
    unit: Literal["S/m", "S/in", "µS/cm"]
