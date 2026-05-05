from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.adiabatic_perfect_fluid_equation_of_state import (
    AdiabaticPerfectFluidEquationOfState,
)
from simscale_sdk_v1.models.simulation.incompressible_perfect_gas_equation_of_state import (
    IncompressiblePerfectGasEquationOfState,
)
from simscale_sdk_v1.models.simulation.peng_robinson_gas_equation_of_state import PengRobinsonGasEquationOfState
from simscale_sdk_v1.models.simulation.perfect_fluid_equation_of_state import PerfectFluidEquationOfState
from simscale_sdk_v1.models.simulation.perfect_gas_equation_of_state import PerfectGasEquationOfState
from simscale_sdk_v1.models.simulation.real_gas_equation_of_state import RealGasEquationOfState
from simscale_sdk_v1.models.simulation.rho_const_equation_of_state import RhoConstEquationOfState

_ONE_OF_H_CONST_THERMO_EQUATION_OF_STATE_VARIANTS: dict[str, type] = {
    "PERFECT_GAS": PerfectGasEquationOfState,
    "REAL_GAS": RealGasEquationOfState,
    "RHO_CONST": RhoConstEquationOfState,
    "PERFECT_FLUID": PerfectFluidEquationOfState,
    "INCOMPRESSIBLE_PERFECT_GAS": IncompressiblePerfectGasEquationOfState,
    "ADIABATIC_PERFECT_FLUID": AdiabaticPerfectFluidEquationOfState,
    "PENG_ROBINSON_GAS": PengRobinsonGasEquationOfState,
}

OneOf_HConstThermoEquationOfState = Annotated[
    Union[
        PerfectGasEquationOfState,
        RealGasEquationOfState,
        RhoConstEquationOfState,
        PerfectFluidEquationOfState,
        IncompressiblePerfectGasEquationOfState,
        AdiabaticPerfectFluidEquationOfState,
        PengRobinsonGasEquationOfState,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_H_CONST_THERMO_EQUATION_OF_STATE_VARIANTS,
        )
    ),
]
