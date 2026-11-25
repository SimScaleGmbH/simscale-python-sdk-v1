from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__angle import Unit_Angle
from simscale_sdk_v1.models.simulation.unit__length import Unit_Length
from simscale_sdk_v1.models.simulation.unit__time import Unit_Time


class VariableGroup_R_PHI_Z_TIME(SimScaleModel):
    t: Unit_Time | None = Field(validation_alias="T", serialization_alias="T", default=None)
    r: Unit_Length | None = Field(validation_alias="R", serialization_alias="R", default=None)
    phi_angle: Unit_Angle | None = Field(validation_alias="PHI_ANGLE", serialization_alias="PHI_ANGLE", default=None)
    z: Unit_Length | None = Field(validation_alias="Z", serialization_alias="Z", default=None)
