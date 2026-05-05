from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle


class GeographicalLocation(SimScaleModel):
    latitude: Dimensional_Angle | None = Field(default=None)
    longitude: Dimensional_Angle | None = Field(default=None)
