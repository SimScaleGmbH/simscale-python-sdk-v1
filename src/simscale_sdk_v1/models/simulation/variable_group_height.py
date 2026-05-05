from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__length import Unit_Length


class VariableGroup_HEIGHT(SimScaleModel):
    height: Unit_Length | None = Field(validation_alias="HEIGHT", serialization_alias="HEIGHT", default=None)
