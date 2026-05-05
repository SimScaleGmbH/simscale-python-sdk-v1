from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__length import Unit_Length


class VariableGroup_X_Y_Z(SimScaleModel):
    x: Unit_Length | None = Field(validation_alias="X", serialization_alias="X", default=None)
    y: Unit_Length | None = Field(validation_alias="Y", serialization_alias="Y", default=None)
    z: Unit_Length | None = Field(validation_alias="Z", serialization_alias="Z", default=None)
