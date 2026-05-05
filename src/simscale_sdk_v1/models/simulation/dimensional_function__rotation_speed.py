from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__rotation_speed_value import (
    OneOf_DimensionalFunction_RotationSpeedValue,
)


class DimensionalFunction_RotationSpeed(SimScaleModel):
    value: OneOf_DimensionalFunction_RotationSpeedValue | None = Field(default=None)
    unit: Literal["rad/s", "°/s", "RPM"]
