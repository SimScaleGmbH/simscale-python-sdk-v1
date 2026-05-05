from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.multifrontal_solver import MultifrontalSolver
from simscale_sdk_v1.models.simulation.mumps_solver import MUMPSSolver

# Choose a linear equation system solver for your calculation:Multfront is a direct solver of the multifrontal type. It is easy to set up and behaves well for most problems.MUMPS is a general purpose direct solver of the multifrontal type. It provides a lot of parameter settings to allow the best fitting to your problems needs.
_ONE_OF__MODAL_SOLVER_SOLVER_VARIANTS: dict[str, type] = {
    "MUMPS": MUMPSSolver,
    "MULTIFRONT": MultifrontalSolver,
}

OneOf_ModalSolverSolver = Annotated[
    Union[MUMPSSolver, MultifrontalSolver],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MODAL_SOLVER_SOLVER_VARIANTS,
        )
    ),
]
