from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__inv_pressure import Dimensional_InvPressure
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class YeohHyperElasticModel(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="YEOH",
        description="Schema name: YeohHyperElasticModel",
    )
    c10: Dimensional_Pressure | None = Field(default=None)
    c20: Dimensional_Pressure | None = Field(default=None)
    c30: Dimensional_Pressure | None = Field(default=None)
    d1: Dimensional_InvPressure | None = Field(default=None)
