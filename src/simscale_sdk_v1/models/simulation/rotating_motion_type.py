from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__rotating_motion_type_rotation import OneOf_RotatingMotionTypeRotation


class RotatingMotionType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ROTATING_MOTION",
        description="Schema name: RotatingMotionType",
    )
    rotation: OneOf_RotatingMotionTypeRotation | None = Field(default=None)
