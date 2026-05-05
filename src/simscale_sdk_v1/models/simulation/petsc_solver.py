from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_petsc_settings import AdvancedPETSCSettings


class PETSCSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="PETSC", description="Schema name: PETSCSolver"
    )
    convergence_threshold: float | None = Field(
        validation_alias="convergenceThreshold",
        serialization_alias="convergenceThreshold",
        default=1e-05,
        description="Set the threshold value for convergence detection for the relative convergence criteria.",
    )
    max_iterations: int | None = Field(
        validation_alias="maxIterations",
        serialization_alias="maxIterations",
        default=0,
        description="Set the maximum number of iterations for the iterative solver. If set to 0 PETSC sets an estimate of the maximum number of iterations.",
    )
    advanced_petsc_settings: AdvancedPETSCSettings | None = Field(
        validation_alias="advancedPetscSettings", serialization_alias="advancedPetscSettings", default=None
    )
