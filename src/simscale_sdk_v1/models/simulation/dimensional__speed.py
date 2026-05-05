from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_Speed(SimScaleModel):
    value: float | None = Field(default=None)
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
