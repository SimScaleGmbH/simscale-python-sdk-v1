from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bounded_gauss_upwind_divergence_scheme import BoundedGaussUpwindDivergenceScheme
from simscale_sdk_v1.models.simulation.gauss_limited_linear1_divergence_scheme import (
    GaussLimitedLinear1DivergenceScheme,
)
from simscale_sdk_v1.models.simulation.gauss_linear_divergence_scheme import GaussLinearDivergenceScheme
from simscale_sdk_v1.models.simulation.gauss_linear_upwind_limited_grad_divergence_scheme import (
    GaussLinearUpwindLimitedGradDivergenceScheme,
)
from simscale_sdk_v1.models.simulation.gauss_linear_upwind_unlimited_divergence_scheme import (
    GaussLinearUpwindUnlimitedDivergenceScheme,
)
from simscale_sdk_v1.models.simulation.gauss_upwind_divergence_scheme import GaussUpwindDivergenceScheme
from simscale_sdk_v1.models.simulation.gauss_vanleer_divergence_scheme import GaussVanleerDivergenceScheme

# With this option, you can choose your desired divergence scheme.
_ONE_OF__DIVERGENCE_SCHEMES_DIV__PHI_ENTHALPY_VARIANTS: dict[str, type] = {
    "GAUSS_LINEAR": GaussLinearDivergenceScheme,
    "GAUSS_LINEARUPWIND_UNLIMITED": GaussLinearUpwindUnlimitedDivergenceScheme,
    "GAUSS_LINEARUPWIND_LIMITEDGRAD": GaussLinearUpwindLimitedGradDivergenceScheme,
    "GAUSS_LIMITEDLINEAR_1": GaussLimitedLinear1DivergenceScheme,
    "BOUNDED_GAUSS_UPWIND": BoundedGaussUpwindDivergenceScheme,
    "GAUSS_UPWIND": GaussUpwindDivergenceScheme,
    "GAUSS_VANLEER": GaussVanleerDivergenceScheme,
}

OneOf_DivergenceSchemesDiv_Phi_enthalpy = Annotated[
    Union[
        GaussLinearDivergenceScheme,
        GaussLinearUpwindUnlimitedDivergenceScheme,
        GaussLinearUpwindLimitedGradDivergenceScheme,
        GaussLimitedLinear1DivergenceScheme,
        BoundedGaussUpwindDivergenceScheme,
        GaussUpwindDivergenceScheme,
        GaussVanleerDivergenceScheme,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIVERGENCE_SCHEMES_DIV__PHI_ENTHALPY_VARIANTS,
        )
    ),
]
