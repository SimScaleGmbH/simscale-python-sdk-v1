from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.gamg_solver import GAMGSolver
from simscale_sdk_v1.models.simulation.pbicg_stab_solver import PBICGStabSolver
from simscale_sdk_v1.models.simulation.smooth_solver import SmoothSolver

_ONE_OF__FLUID_SOLVERS_VOLTAGE_SOLVER_VARIANTS: dict[str, type] = {
    "GAMG": GAMGSolver,
    "PBICGStab": PBICGStabSolver,
    "SMOOTH": SmoothSolver,
}

OneOf_FluidSolversVoltageSolver = Annotated[
    Union[GAMGSolver, PBICGStabSolver, SmoothSolver],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_SOLVERS_VOLTAGE_SOLVER_VARIANTS,
        )
    ),
]
