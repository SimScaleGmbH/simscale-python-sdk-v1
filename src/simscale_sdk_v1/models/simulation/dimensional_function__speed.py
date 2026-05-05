from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__speed_value import (
    OneOf_DimensionalFunction_SpeedValue,
)


class DimensionalFunction_Speed(SimScaleModel):
    value: OneOf_DimensionalFunction_SpeedValue | None = Field(default=None)
    unit: Literal[
        "m/s",
        "in/s",
        "m/min",
        "m/h",
        "mm/s",
        "mm/min",
        "mm/h",
        "cm/s",
        "cm/min",
        "cm/h",
        "km/h",
        "ft/s",
        "ft/min",
        "ft/h",
        "in/min",
        "in/h",
        "mph",
        "kn",
    ]
