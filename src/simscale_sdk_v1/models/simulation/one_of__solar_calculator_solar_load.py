from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.custom_solar_load import CustomSolarLoad
from simscale_sdk_v1.models.simulation.fair_weather_conditions import FairWeatherConditions

# Solar load in solar radiation model. Diffuse solar load affects all walls with a derived heat flux boundary condition externally if the outer surface absorptivity is greater than  zero. Direct solar load affects all walls either externally or internally if these are not shadowed by other walls, are non-transparent and have an absorptivity greater than zero.  Custom: Define diffusive and directed solar load directly.Fair weather conditions: Define the external and internal solar load by a number of coefficients in the Fair weather condtions model.This assumes the Z-vector to point upwards into the sky.
_ONE_OF__SOLAR_CALCULATOR_SOLAR_LOAD_VARIANTS: dict[str, type] = {
    "CUSTOM_SOLAR_LOAD": CustomSolarLoad,
    "FAIR_WEATHER_CONDITIONS": FairWeatherConditions,
}

OneOf_SolarCalculatorSolarLoad = Annotated[
    Union[CustomSolarLoad, FairWeatherConditions],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLAR_CALCULATOR_SOLAR_LOAD_VARIANTS,
        )
    ),
]
