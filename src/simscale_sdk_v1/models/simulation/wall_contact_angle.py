from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle


class WallContactAngle(SimScaleModel):
    enable_wall_contact_angle: bool | None = Field(
        validation_alias="enableWallContactAngle", serialization_alias="enableWallContactAngle", default=False
    )
    associated_phase: Literal["PHASE_0", "PHASE_1"] | None = Field(
        validation_alias="associatedPhase", serialization_alias="associatedPhase", default="PHASE_0"
    )
    contact_angle: Dimensional_Angle | None = Field(
        validation_alias="contactAngle", serialization_alias="contactAngle", default=None
    )
