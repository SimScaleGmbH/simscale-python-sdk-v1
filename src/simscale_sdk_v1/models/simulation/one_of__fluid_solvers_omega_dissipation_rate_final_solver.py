from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.pbicg_solver import PBICGSolver
from simscale_sdk_v1.models.simulation.pbicg_stab_solver import PBICGStabSolver
from simscale_sdk_v1.models.simulation.smooth_solver import SmoothSolver

_ONE_OF__FLUID_SOLVERS_OMEGA_DISSIPATION_RATE_FINAL_SOLVER_VARIANTS: dict[str, type] = {
    "PBICG": PBICGSolver,
    "PBICGStab": PBICGStabSolver,
    "SMOOTH": SmoothSolver,
}

OneOf_FluidSolversOmegaDissipationRateFinalSolver = Annotated[
    Union[PBICGSolver, PBICGStabSolver, SmoothSolver],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_SOLVERS_OMEGA_DISSIPATION_RATE_FINAL_SOLVER_VARIANTS,
        )
    ),
]
