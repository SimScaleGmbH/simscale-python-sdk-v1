from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.global_velocity_type import GlobalVelocityType


class VelocityResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VELOCITY",
        description="Schema name: VelocityResultControlItem",
    )
    name: str | None = Field(default=None)
    velocity_type: GlobalVelocityType | None = Field(
        validation_alias="velocityType", serialization_alias="velocityType", default=None
    )
