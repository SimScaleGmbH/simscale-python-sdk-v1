from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_resistivity_value import (
    OneOf_DimensionalFunction_ElectricResistivityValue,
)


class DimensionalFunction_ElectricResistivity(SimScaleModel):
    value: OneOf_DimensionalFunction_ElectricResistivityValue | None = Field(default=None)
    unit: Literal["Ω·m", "Ω·in"]
