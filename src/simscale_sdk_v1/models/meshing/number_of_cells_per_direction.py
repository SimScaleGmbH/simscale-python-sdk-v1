from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class NumberOfCellsPerDirection(SimScaleModel):
    x: int | None = Field(default=40)
    y: int | None = Field(default=40)
    z: int | None = Field(default=40)
