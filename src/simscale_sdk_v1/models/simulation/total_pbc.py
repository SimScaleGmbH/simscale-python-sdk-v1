from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class TotalPBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_PRESSURE",
        description="Schema name: TotalPBC",
    )
    total_pressure: DimensionalFunction_Pressure | None = Field(
        validation_alias="totalPressure", serialization_alias="totalPressure", default=None
    )
