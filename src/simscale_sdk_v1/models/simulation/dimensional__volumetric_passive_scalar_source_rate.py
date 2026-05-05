from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Dimensional_VolumetricPassiveScalarSourceRate(SimScaleModel):
    value: float | None = Field(default=None)
    unit: Literal["1/(m³·s)", "1/(in³·s)"]
