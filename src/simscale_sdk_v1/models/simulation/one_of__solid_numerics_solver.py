from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.chronos_solver import ChronosSolver
from simscale_sdk_v1.models.simulation.multifrontal_solver import MultifrontalSolver
from simscale_sdk_v1.models.simulation.mumps_solver import MUMPSSolver
from simscale_sdk_v1.models.simulation.petsc_solver import PETSCSolver

_ONE_OF__SOLID_NUMERICS_SOLVER_VARIANTS: dict[str, type] = {
    "MUMPS": MUMPSSolver,
    "MULTIFRONT": MultifrontalSolver,
    "PETSC": PETSCSolver,
    "CHRONOS": ChronosSolver,
}

OneOf_SolidNumericsSolver = Annotated[
    Union[MUMPSSolver, MultifrontalSolver, PETSCSolver, ChronosSolver],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_NUMERICS_SOLVER_VARIANTS,
        )
    ),
]
