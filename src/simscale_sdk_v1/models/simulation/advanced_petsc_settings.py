from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__advanced_petsc_settings_preconditioner import (
    OneOf_AdvancedPETSCSettingsPreconditioner,
)


class AdvancedPETSCSettings(SimScaleModel):
    force_symmetric: bool | None = Field(
        validation_alias="forceSymmetric",
        serialization_alias="forceSymmetric",
        default=False,
        description="Choose if you want to enforce a symmetric matrix.",
    )
    algorithm: Literal["CG", "CR", "GCR", "GMRES"] | None = Field(
        default="GMRES",
        description="Choose the iterative solver method: FGMRES: Flexible Minimal Generalised RESidual, best compromise between robustness and computational speed.CG: Conjugate Gradient, only useful for symmetric matricesCR: Conjugate Residual, only useful for symmetric matricesGCR: Generalised Conjugate Residual, treats general matricesAll available methods are of Krylov type.",
    )
    preconditioner: OneOf_AdvancedPETSCSettingsPreconditioner | None = Field(default=None)
    distributed_matrix_storage: bool | None = Field(
        validation_alias="distributedMatrixStorage",
        serialization_alias="distributedMatrixStorage",
        default=True,
        description="Choose this parameter as true to ensure that the system matrix saving is distributed among the processors of the computation. If multiple cores are used only the relevant part for each core is saved. If it is set to false the whole matrix is saved for each processor. Enabling this can significantly reductions in memory consumption, but introduces numerical instability in rare occasions.",
    )
