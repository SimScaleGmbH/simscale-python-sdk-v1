from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__temperature_value import (
    OneOf_DimensionalFunction_TemperatureValue,
)


class DimensionalFunction_Temperature(SimScaleModel):
    value: OneOf_DimensionalFunction_TemperatureValue | None = Field(default=None)
    unit: Literal["°C", "°F", "K"]
