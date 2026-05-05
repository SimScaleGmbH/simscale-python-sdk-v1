from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__rotating_sbm_rotation import OneOf_RotatingSBMRotation


class RotatingSBM(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ROTATING_MOTION",
        description="Schema name: RotatingSBM",
    )
    name: str | None = Field(default=None)
    rotation: OneOf_RotatingSBMRotation | None = Field(default=None)
