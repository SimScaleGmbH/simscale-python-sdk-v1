from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.pbicg_solver import PBICGSolver
from simscale_sdk_v1.models.simulation.smooth_solver import SmoothSolver

_ONE_OF__TRUE_SEMI_IMPLICIT_SOLVER_VARIANTS: dict[str, type] = {
    "PBICG": PBICGSolver,
    "SMOOTH": SmoothSolver,
}

OneOf_TrueSemiImplicitSolver = Annotated[
    Union[PBICGSolver, SmoothSolver],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__TRUE_SEMI_IMPLICIT_SOLVER_VARIANTS,
        )
    ),
]
