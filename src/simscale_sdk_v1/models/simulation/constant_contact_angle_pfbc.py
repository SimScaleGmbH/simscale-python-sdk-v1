from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle


class ConstantContactAnglePFBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONSTANT_CONTACT_ANGLE",
        description="Schema name: ConstantContactAnglePFBC",
    )
    equilibrium_contact_angle: Dimensional_Angle | None = Field(
        validation_alias="equilibriumContactAngle", serialization_alias="equilibriumContactAngle", default=None
    )
    limit: Literal["GRADIENT", "NONE", "PHASE_FRACTION", "ZERO_GRADIENT"] | None = Field(default="NONE")
