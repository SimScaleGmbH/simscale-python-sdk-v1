from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.dic_preconditioner import DICPreconditioner
from simscale_sdk_v1.models.simulation.dilu_preconditioner import DILUPreconditioner
from simscale_sdk_v1.models.simulation.ilu_cp_preconditioner import ILUCpPreconditioner

# Choose a preconditioner for your solver. A preconditioner improves the convergence speed of your system. Therefore, it is generally recommended. DILU is a very common diagonal incomplete lower-upper decomposition preconditioner.
_ONE_OF_PBICG_STAB_SOLVER_PRECONDITIONER_VARIANTS: dict[str, type] = {
    "DILU": DILUPreconditioner,
    "DIC": DICPreconditioner,
    "ILUCP": ILUCpPreconditioner,
}

OneOf_PBICGStabSolverPreconditioner = Annotated[
    Union[DILUPreconditioner, DICPreconditioner, ILUCpPreconditioner],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF_PBICG_STAB_SOLVER_PRECONDITIONER_VARIANTS,
        )
    ),
]
