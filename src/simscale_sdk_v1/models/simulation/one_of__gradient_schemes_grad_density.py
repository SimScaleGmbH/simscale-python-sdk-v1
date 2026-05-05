from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.celllimited_gauss_linear_gradient_scheme import (
    CelllimitedGaussLinearGradientScheme,
)
from simscale_sdk_v1.models.simulation.celllimited_least_squares_gradient_scheme import (
    CelllimitedLeastSquaresGradientScheme,
)
from simscale_sdk_v1.models.simulation.fourth_gradient_scheme import FourthGradientScheme
from simscale_sdk_v1.models.simulation.gauss_linear_gradient_scheme import GaussLinearGradientScheme
from simscale_sdk_v1.models.simulation.leastsquares_gradient_scheme import LeastsquaresGradientScheme

# With this option, you can choose your desired gradient scheme:If you are unsure, try Gauss linear first.If you require a higher-order scheme you can use leastSquares.
_ONE_OF__GRADIENT_SCHEMES_GRAD_DENSITY_VARIANTS: dict[str, type] = {
    "GAUSS_LINEAR": GaussLinearGradientScheme,
    "CELLLIMITED_GAUSS_LINEAR": CelllimitedGaussLinearGradientScheme,
    "CELLLIMITED_LEASTSQUARES": CelllimitedLeastSquaresGradientScheme,
    "FOURTH": FourthGradientScheme,
    "LEASTSQUARES": LeastsquaresGradientScheme,
}

OneOf_GradientSchemesGrad_density = Annotated[
    Union[
        GaussLinearGradientScheme,
        CelllimitedGaussLinearGradientScheme,
        CelllimitedLeastSquaresGradientScheme,
        FourthGradientScheme,
        LeastsquaresGradientScheme,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__GRADIENT_SCHEMES_GRAD_DENSITY_VARIANTS,
        )
    ),
]
