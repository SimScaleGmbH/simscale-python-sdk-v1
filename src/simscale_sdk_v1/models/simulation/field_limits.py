from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__density import Dimensional_Density
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class FieldLimits(SimScaleModel):
    lower_density_bound: Dimensional_Density | None = Field(
        validation_alias="lowerDensityBound", serialization_alias="lowerDensityBound", default=None
    )
    upper_density_bound: Dimensional_Density | None = Field(
        validation_alias="upperDensityBound", serialization_alias="upperDensityBound", default=None
    )
    lower_pressure_bound: Dimensional_Pressure | None = Field(
        validation_alias="lowerPressureBound", serialization_alias="lowerPressureBound", default=None
    )
    upper_pressure_bound: Dimensional_Pressure | None = Field(
        validation_alias="upperPressureBound", serialization_alias="upperPressureBound", default=None
    )
    lower_temperature_bound: Dimensional_Temperature | None = Field(
        validation_alias="lowerTemperatureBound", serialization_alias="lowerTemperatureBound", default=None
    )
    upper_temperature_bound: Dimensional_Temperature | None = Field(
        validation_alias="upperTemperatureBound", serialization_alias="upperTemperatureBound", default=None
    )
