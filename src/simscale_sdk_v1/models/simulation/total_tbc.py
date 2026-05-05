from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature


class TotalTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_TEMPERATURE",
        description="Schema name: TotalTBC",
    )
    total_temperature: Dimensional_Temperature | None = Field(
        validation_alias="totalTemperature", serialization_alias="totalTemperature", default=None
    )
    total_temperature_function: DimensionalFunction_Temperature | None = Field(
        validation_alias="totalTemperatureFunction", serialization_alias="totalTemperatureFunction", default=None
    )
    specific_heat_ratio: float | None = Field(
        validation_alias="specificHeatRatio", serialization_alias="specificHeatRatio", default=1.4
    )
