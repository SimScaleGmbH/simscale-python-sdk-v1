from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__electric_current_value import (
    OneOf_DimensionalFunction_ElectricCurrentValue,
)


class DimensionalFunction_ElectricCurrent(SimScaleModel):
    value: OneOf_DimensionalFunction_ElectricCurrentValue | None = Field(default=None)
    unit: Literal["A"]
