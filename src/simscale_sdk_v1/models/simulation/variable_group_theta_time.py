from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__angle import Unit_Angle
from simscale_sdk_v1.models.simulation.unit__time import Unit_Time


class VariableGroup_THETA_TIME(SimScaleModel):
    t: Unit_Time | None = Field(validation_alias="T", serialization_alias="T", default=None)
    theta_angle: Unit_Angle | None = Field(
        validation_alias="THETA_ANGLE", serialization_alias="THETA_ANGLE", default=None
    )
