from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.custom_fraction_body_surface import CustomFractionBodySurface
from simscale_sdk_v1.models.simulation.sitting_fraction_body_surface import SittingFractionBodySurface
from simscale_sdk_v1.models.simulation.standing_fraction_body_surface import StandingFractionBodySurface

# The fraction of body exposed to radiation (feff) refers to the portion of the body in the range [0, 1] exposed to direct solar radiation (e.g. 0.696 for a seated person and 0.725 for a standing person)
_ONE_OF__MRT_SOLAR_PARAMETERS_FRACTION_BODY_SURFACE_VARIANTS: dict[str, type] = {
    "SITTING_FRACTION_BODY_SURFACE": SittingFractionBodySurface,
    "STANDING_FRACTION_BODY_SURFACE": StandingFractionBodySurface,
    "CUSTOM_FRACTION_BODY_SURFACE": CustomFractionBodySurface,
}

OneOf_MrtSolarParametersFractionBodySurface = Annotated[
    Union[SittingFractionBodySurface, StandingFractionBodySurface, CustomFractionBodySurface],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MRT_SOLAR_PARAMETERS_FRACTION_BODY_SURFACE_VARIANTS,
        )
    ),
]
