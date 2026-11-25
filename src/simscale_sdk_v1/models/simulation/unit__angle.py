from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Unit_Angle(SimScaleModel):
    value: float | None = Field(default=None)
    unit: Literal["rad", "°"] | None = Field(default=None)
