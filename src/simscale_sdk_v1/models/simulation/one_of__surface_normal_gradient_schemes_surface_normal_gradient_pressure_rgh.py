from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.corrected_surface_normal_gradient_scheme import (
    CorrectedSurfaceNormalGradientScheme,
)
from simscale_sdk_v1.models.simulation.limited_surface_normal_gradient_scheme import LimitedSurfaceNormalGradientScheme
from simscale_sdk_v1.models.simulation.uncorrected_surface_normal_gradient_scheme import (
    UncorrectedSurfaceNormalGradientScheme,
)

# A surface normal gradient is the component, normal to the face, of the gradient of values at the centres of the 2 cells connected through that face. Choose your desired scheme.
_ONE_OF__SURFACE_NORMAL_GRADIENT_SCHEMES_SURFACE_NORMAL_GRADIENT_PRESSURE_RGH_VARIANTS: dict[str, type] = {
    "CORRECTED": CorrectedSurfaceNormalGradientScheme,
    "UNCORRECTED": UncorrectedSurfaceNormalGradientScheme,
    "LIMITED": LimitedSurfaceNormalGradientScheme,
}

OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_pressureRgh = Annotated[
    Union[
        CorrectedSurfaceNormalGradientScheme, UncorrectedSurfaceNormalGradientScheme, LimitedSurfaceNormalGradientScheme
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SURFACE_NORMAL_GRADIENT_SCHEMES_SURFACE_NORMAL_GRADIENT_PRESSURE_RGH_VARIANTS,
        )
    ),
]
