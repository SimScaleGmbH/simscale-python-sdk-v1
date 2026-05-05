from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__inv_pressure import Dimensional_InvPressure
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class MooneyRivlinHyperElasticModel(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MOONEY_RIVLIN",
        description="Schema name: MooneyRivlinHyperElasticModel",
    )
    c10: Dimensional_Pressure | None = Field(default=None)
    c01: Dimensional_Pressure | None = Field(default=None)
    d1: Dimensional_InvPressure | None = Field(default=None)
