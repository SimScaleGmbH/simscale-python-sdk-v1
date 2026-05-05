from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.gauss_linear_corrected_laplacian_scheme import (
    GaussLinearCorrectedLaplacianScheme,
)
from simscale_sdk_v1.models.simulation.gauss_linear_limited_corrected_laplacian_scheme import (
    GaussLinearLimitedCorrectedLaplacianScheme,
)
from simscale_sdk_v1.models.simulation.gauss_linear_uncorrected_laplacian_scheme import (
    GaussLinearUncorrectedLaplacianScheme,
)

# With this option you can choose your desired laplacian scheme.
_ONE_OF__LAPLACIAN_SCHEMES_LAPLACIAN_RHO_1_A_U_PRESSURE_VARIANTS: dict[str, type] = {
    "GAUSS_LINEAR_CORRECTED": GaussLinearCorrectedLaplacianScheme,
    "GAUSS_LINEAR_LIMITED_CORRECTED": GaussLinearLimitedCorrectedLaplacianScheme,
    "GAUSS_LINEAR_UNCORRECTED": GaussLinearUncorrectedLaplacianScheme,
}

OneOf_LaplacianSchemesLaplacian_rho_1_A_U_pressure = Annotated[
    Union[
        GaussLinearCorrectedLaplacianScheme,
        GaussLinearLimitedCorrectedLaplacianScheme,
        GaussLinearUncorrectedLaplacianScheme,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__LAPLACIAN_SCHEMES_LAPLACIAN_RHO_1_A_U_PRESSURE_VARIANTS,
        )
    ),
]
