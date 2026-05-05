from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure


class TotalPressurePressureType(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_PRESSURE",
        description="Schema name: TotalPressurePressureType",
    )
    pressure_value: Dimensional_Pressure | None = Field(
        validation_alias="pressureValue", serialization_alias="pressureValue", default=None
    )
