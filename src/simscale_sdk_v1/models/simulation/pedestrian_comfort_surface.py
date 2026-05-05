from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.one_of__pedestrian_comfort_surface_ground import (
    OneOf_PedestrianComfortSurfaceGround,
)


class PedestrianComfortSurface(SimScaleModel):
    name: str | None = Field(default=None)
    height_above_ground: Dimensional_Length | None = Field(
        validation_alias="heightAboveGround", serialization_alias="heightAboveGround", default=None
    )
    ground: OneOf_PedestrianComfortSurfaceGround | None = Field(default=None)
