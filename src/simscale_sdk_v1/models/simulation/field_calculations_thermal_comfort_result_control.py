from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.mrt_solar_parameters import MrtSolarParameters


class FieldCalculationsThermalComfortResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="THERMAL_COMFORT",
        description="Schema name: FieldCalculationsThermalComfortResultControl",
    )
    name: str | None = Field(default=None)
    clothing_coefficient_factor: float | None = Field(
        validation_alias="clothingCoefficientFactor", serialization_alias="clothingCoefficientFactor", default=1
    )
    metabolic_rate_factor: float | None = Field(
        validation_alias="metabolicRateFactor", serialization_alias="metabolicRateFactor", default=1
    )
    relative_humidity_factor: float | None = Field(
        validation_alias="relativeHumidityFactor", serialization_alias="relativeHumidityFactor", default=50
    )
    mrt_solar_parameters: MrtSolarParameters | None = Field(
        validation_alias="mrtSolarParameters", serialization_alias="mrtSolarParameters", default=None
    )
