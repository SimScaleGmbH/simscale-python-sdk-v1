from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__power_value import (
    OneOf_DimensionalFunction_PowerValue,
)


class DimensionalFunction_Power(SimScaleModel):
    value: OneOf_DimensionalFunction_PowerValue | None = Field(default=None)
    unit: Literal["W", "Btu/s", "kW", "MW", "HP", "CV", "Btu/min", "Btu/h"]
