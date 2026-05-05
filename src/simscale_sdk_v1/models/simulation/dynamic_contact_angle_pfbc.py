from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle


class DynamicContactAnglePFBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DYNAMIC_CONTACT_ANGLE",
        description="Schema name: DynamicContactAnglePFBC",
    )
    equilibrium_contact_angle: Dimensional_Angle | None = Field(
        validation_alias="equilibriumContactAngle", serialization_alias="equilibriumContactAngle", default=None
    )
    advancing_contact_angle: Dimensional_Angle | None = Field(
        validation_alias="advancingContactAngle", serialization_alias="advancingContactAngle", default=None
    )
    receding_contact_angle: Dimensional_Angle | None = Field(
        validation_alias="recedingContactAngle", serialization_alias="recedingContactAngle", default=None
    )
    velocity_scale_of_contact_angle: float | None = Field(
        validation_alias="velocityScaleOfContactAngle", serialization_alias="velocityScaleOfContactAngle", default=1
    )
    limit: Literal["GRADIENT", "NONE", "PHASE_FRACTION", "ZERO_GRADIENT"] | None = Field(default="NONE")
