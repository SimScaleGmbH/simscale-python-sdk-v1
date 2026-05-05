from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__solar_calculator_solar_load import OneOf_SolarCalculatorSolarLoad
from simscale_sdk_v1.models.simulation.one_of__solar_calculator_sun_direction import OneOf_SolarCalculatorSunDirection


class SolarCalculator(SimScaleModel):
    sun_direction: OneOf_SolarCalculatorSunDirection | None = Field(
        validation_alias="sunDirection", serialization_alias="sunDirection", default=None
    )
    solar_load: OneOf_SolarCalculatorSolarLoad | None = Field(
        validation_alias="solarLoad", serialization_alias="solarLoad", default=None
    )
