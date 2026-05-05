from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.perfect_gas_equation_of_state import PerfectGasEquationOfState
from simscale_sdk_v1.models.simulation.rho_const_equation_of_state import RhoConstEquationOfState

_ONE_OF__FLUID_COMPRESSIBLE_MATERIAL_EQUATION_OF_STATE_VARIANTS: dict[str, type] = {
    "PERFECT_GAS": PerfectGasEquationOfState,
    "RHO_CONST": RhoConstEquationOfState,
}

OneOf_FluidCompressibleMaterialEquationOfState = Annotated[
    Union[PerfectGasEquationOfState, RhoConstEquationOfState],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_COMPRESSIBLE_MATERIAL_EQUATION_OF_STATE_VARIANTS,
        )
    ),
]
