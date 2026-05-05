from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__dimensionless import Unit_Dimensionless
from simscale_sdk_v1.models.simulation.unit__temperature import Unit_Temperature


class VariableGroup_TEMP_STRAIN(SimScaleModel):
    e: Unit_Dimensionless | None = Field(validation_alias="E", serialization_alias="E", default=None)
    temperature: Unit_Temperature | None = Field(
        validation_alias="Temperature", serialization_alias="Temperature", default=None
    )
