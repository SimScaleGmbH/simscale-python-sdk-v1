from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.custom_sun_direction import CustomSunDirection
from simscale_sdk_v1.models.simulation.time_and_place_sun_direction import TimeAndPlaceSunDirection

# Sun direction in the solar radiation model. Custom: Define the sun direction vector directly.Time and place: Set the sun direction by defining a location, a date and a time. This assumes the Z-vector to point upwards into the sky.
_ONE_OF__SOLAR_CALCULATOR_SUN_DIRECTION_VARIANTS: dict[str, type] = {
    "TIME_AND_PLACE": TimeAndPlaceSunDirection,
    "CUSTOM_SOLAR_DIRECTION": CustomSunDirection,
}

OneOf_SolarCalculatorSunDirection = Annotated[
    Union[TimeAndPlaceSunDirection, CustomSunDirection],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLAR_CALCULATOR_SUN_DIRECTION_VARIANTS,
        )
    ),
]
