from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.vector3_d import Vector3D


class SeedSettings(SimScaleModel):
    center: Vector3D
    normal: Vector3D
    horizontal_dimension: int = Field(
        validation_alias="horizontalDimension",
        serialization_alias="horizontalDimension",
        default=10,
        description="Number of seed points in the horizontal direction.",
    )
    vertical_dimension: int = Field(
        validation_alias="verticalDimension",
        serialization_alias="verticalDimension",
        default=10,
        description="Number of seed points in the vertical direction.",
    )
    spacing: float | None = Field(
        default=None, description="The distance between the seed points. Default is size * 4."
    )
    size: float | None = Field(
        default=None,
        description="The radius of the particle trace geometry (cylinder, sphere, comet). Default is the extent of the bounding box of the moddel divided by 800.",
    )
