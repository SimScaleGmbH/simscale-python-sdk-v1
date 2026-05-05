from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_energy_value import (
    OneOf_DimensionalFunction_SpecificEnergyValue,
)


class DimensionalFunction_SpecificEnergy(SimScaleModel):
    value: OneOf_DimensionalFunction_SpecificEnergyValue | None = Field(default=None)
    unit: Literal["J/kg", "Btu/lb"]
