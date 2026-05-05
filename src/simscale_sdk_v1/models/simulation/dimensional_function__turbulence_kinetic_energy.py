from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__turbulence_kinetic_energy_value import (
    OneOf_DimensionalFunction_TurbulenceKineticEnergyValue,
)


class DimensionalFunction_TurbulenceKineticEnergy(SimScaleModel):
    value: OneOf_DimensionalFunction_TurbulenceKineticEnergyValue | None = Field(default=None)
    unit: Literal["m²/s²", "Btu/lb"]
