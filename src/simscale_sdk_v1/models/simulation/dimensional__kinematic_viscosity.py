from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_KinematicViscosity(SimScaleModel):
    value: float | None = Field(default=None)
    unit: Literal["m²/s", "lbf·s·in/lb", "ft²/s", "in²/s"]
