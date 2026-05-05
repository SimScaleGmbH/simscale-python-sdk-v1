from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.mumps_direct_solver import MumpsDirectSolver
from simscale_sdk_v1.models.simulation.pardiso_direct_solver import PardisoDirectSolver
from simscale_sdk_v1.models.simulation.sparse_iterative import SparseIterative

# Defines the numerical method used to solve the linear system of equations $Ax=b$ within each iteration. Choosing the right solver depends on the model size, available memory, and the presence of instabilities.Direct (MUMPS): A robust, multi-frontal direct solver suitable for a wide range of problems, especially those with material nonlinearities or contact. It is generally more memory-intensive than iterative solvers but highly reliable for complex nonlinearities.Direct (Pardiso): A high-performance direct solver optimized for multi-core CPUs, offering efficient memory usage and fast solution times for large-scale linear and nonlinear problems. It is a good alternative to MUMPS for large models.Iterative: Best for very large, bulky models due to lower memory demand. This solver might be less robust in highly nonlinear scenarios compared to the direct solvers.
_ONE_OF__MARC_LINEAR_SOLVER_SETTINGS_LINEAR_SOLVER_VARIANTS: dict[str, type] = {
    "MUMPS_DIRECT": MumpsDirectSolver,
    "PARDISO_DIRECT": PardisoDirectSolver,
    "SPARSE_ITERATIVE": SparseIterative,
}

OneOf_MarcLinearSolverSettingsLinearSolver = Annotated[
    Union[MumpsDirectSolver, PardisoDirectSolver, SparseIterative],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__MARC_LINEAR_SOLVER_SETTINGS_LINEAR_SOLVER_VARIANTS,
        )
    ),
]
