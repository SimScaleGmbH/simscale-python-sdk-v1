from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_MassFlowRate(SimScaleModel):
    value: float | None = Field(default=None)
    unit: Literal[
        "kg/s", "lb/s", "kg/min", "kg/h", "g/s", "g/min", "g/h", "lb/min", "lb/h", "slug/s", "slug/min", "slug/h"
    ]
