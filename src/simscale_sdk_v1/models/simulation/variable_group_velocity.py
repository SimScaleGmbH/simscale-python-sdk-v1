from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__speed import Unit_Speed


class VariableGroup_VELOCITY(SimScaleModel):
    velocity: Unit_Speed | None = Field(validation_alias="VELOCITY", serialization_alias="VELOCITY", default=None)
