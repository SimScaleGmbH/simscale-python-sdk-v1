from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__volumetric_power_value import (
    OneOf_DimensionalFunction_VolumetricPowerValue,
)


class DimensionalFunction_VolumetricPower(SimScaleModel):
    value: OneOf_DimensionalFunction_VolumetricPowerValue | None = Field(default=None)
    unit: Literal["W/m³", "Btu/(s·in³)"]
