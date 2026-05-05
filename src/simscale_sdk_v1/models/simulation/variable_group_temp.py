from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__temperature import Unit_Temperature


class VariableGroup_TEMP(SimScaleModel):
    temperature: Unit_Temperature | None = Field(
        validation_alias="Temperature", serialization_alias="Temperature", default=None
    )
