from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_MassAreaDensity(SimScaleModel):
    value: float | None = Field(default=None)
    unit: Literal["kg/m²", "lb/in²", "g/m²", "gr/ft²"]
