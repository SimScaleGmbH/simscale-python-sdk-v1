from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.gauss_linear_divergence_scheme import GaussLinearDivergenceScheme
from simscale_sdk_v1.models.simulation.gauss_linear_upwind_v_unlimited_divergence_scheme import (
    GaussLinearUpwindVUnlimitedDivergenceScheme,
)

# With this option, you can choose your desired divergence scheme.
_ONE_OF__DIVERGENCE_SCHEMES_DIV_TAU_MC_VARIANTS: dict[str, type] = {
    "GAUSS_LINEAR": GaussLinearDivergenceScheme,
    "GAUSS_LINEARUPWINDV_UNLIMITED": GaussLinearUpwindVUnlimitedDivergenceScheme,
}

OneOf_DivergenceSchemesDiv_tauMC = Annotated[
    Union[GaussLinearDivergenceScheme, GaussLinearUpwindVUnlimitedDivergenceScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__DIVERGENCE_SCHEMES_DIV_TAU_MC_VARIANTS,
        )
    ),
]
