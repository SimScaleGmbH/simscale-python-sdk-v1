from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cubic_interpolation_scheme import CubicInterpolationScheme
from simscale_sdk_v1.models.simulation.linear_interpolation_scheme import LinearInterpolationScheme

# With this option you can choose your desired interpolation scheme.
_ONE_OF__INTERPOLATION_SCHEMES_INTERPOLATE_RHO_R_AU_VARIANTS: dict[str, type] = {
    "CUBIC": CubicInterpolationScheme,
    "LINEAR": LinearInterpolationScheme,
}

OneOf_InterpolationSchemesInterpolate_rho_rAU = Annotated[
    Union[CubicInterpolationScheme, LinearInterpolationScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__INTERPOLATION_SCHEMES_INTERPOLATE_RHO_R_AU_VARIANTS,
        )
    ),
]
