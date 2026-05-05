from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_field_strength_value import (
    OneOf_DimensionalFunction_ElectricFieldStrengthValue,
)


class DimensionalFunction_ElectricFieldStrength(SimScaleModel):
    value: OneOf_DimensionalFunction_ElectricFieldStrengthValue | None = Field(default=None)
    unit: Literal["V/m", "V/in"]
