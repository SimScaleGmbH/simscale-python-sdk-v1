from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed
from simscale_sdk_v1.models.simulation.wall_contact_angle import WallContactAngle


class MovingWallVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MOVING_WALL_VELOCITY",
        description="Schema name: MovingWallVBC",
    )
    value: DimensionalVector_Speed | None = Field(default=None)
    turbulence_wall: Literal["WALL_FUNCTION", "FULL_RESOLUTION"] | None = Field(
        validation_alias="turbulenceWall", serialization_alias="turbulenceWall", default="WALL_FUNCTION"
    )
    orientation_reference: Literal["GEOMETRY", "FLOW_DOMAIN"] | None = Field(
        validation_alias="orientationReference", serialization_alias="orientationReference", default="FLOW_DOMAIN"
    )
    wall_contact_model: list[WallContactAngle] | None = Field(
        validation_alias="wallContactModel", serialization_alias="wallContactModel", default=None
    )
