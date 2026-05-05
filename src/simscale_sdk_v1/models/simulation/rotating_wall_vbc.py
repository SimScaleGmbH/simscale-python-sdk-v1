from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.angular_rotation import AngularRotation
from simscale_sdk_v1.models.simulation.wall_contact_angle import WallContactAngle


class RotatingWallVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ROTATING_WALL_VELOCITY",
        description="Schema name: RotatingWallVBC",
    )
    rotation: AngularRotation | None = Field(default=None)
    turbulence_wall: Literal["WALL_FUNCTION", "FULL_RESOLUTION"] | None = Field(
        validation_alias="turbulenceWall", serialization_alias="turbulenceWall", default="WALL_FUNCTION"
    )
    wall_contact_model: list[WallContactAngle] | None = Field(
        validation_alias="wallContactModel", serialization_alias="wallContactModel", default=None
    )
