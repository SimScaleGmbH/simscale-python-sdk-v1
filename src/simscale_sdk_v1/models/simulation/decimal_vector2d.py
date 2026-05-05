from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DecimalVector2d(SimScaleModel):
    x: float | None = Field(default=None)
    y: float | None = Field(default=None)
