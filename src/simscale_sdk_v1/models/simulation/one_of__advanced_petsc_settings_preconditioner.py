from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.inactive_preconditioner import InactivePreconditioner
from simscale_sdk_v1.models.simulation.incomplete_preconditioner_v33 import IncompletePreconditionerV33
from simscale_sdk_v1.models.simulation.jacobi_preconditioner import JacobiPreconditioner
from simscale_sdk_v1.models.simulation.mumps_preconditoner import MUMPSPreconditoner
from simscale_sdk_v1.models.simulation.sor_preconditioner import SorPreconditioner

# Choose the preconditioner for the iterative solver:incomplete LDLT performs an incomplete Cholesky decomposition.MUMPS LDLT performs a complete Cholesky decomposition in single precision via the MUMPS package.Jacobi is a standard diagonal preconditioner.SOR uses the method of Successive Over-Relaxation.
_ONE_OF__ADVANCED_PETSC_SETTINGS_PRECONDITIONER_VARIANTS: dict[str, type] = {
    "MUMPS_LDLT": MUMPSPreconditoner,
    "INCOMPLETE_LDLT_V33": IncompletePreconditionerV33,
    "JACOBI": JacobiPreconditioner,
    "SOR": SorPreconditioner,
    "INACTIVE": InactivePreconditioner,
}

OneOf_AdvancedPETSCSettingsPreconditioner = Annotated[
    Union[
        MUMPSPreconditoner, IncompletePreconditionerV33, JacobiPreconditioner, SorPreconditioner, InactivePreconditioner
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_PETSC_SETTINGS_PRECONDITIONER_VARIANTS,
        )
    ),
]
