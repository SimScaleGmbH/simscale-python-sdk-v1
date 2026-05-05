from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class RefinementLevel(SimScaleModel):
    distance: Dimensional_Length | None = Field(default=None)
    level: int | None = Field(default=1)
