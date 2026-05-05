from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of_pcg_solver_preconditioner import OneOf_PCGSolverPreconditioner


class PCGSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="PCG", description="Schema name: PCGSolver"
    )
    absolute_tolerance: float | None = Field(
        validation_alias="absoluteTolerance",
        serialization_alias="absoluteTolerance",
        default=None,
        description="Define the absolute tolerance for the residual. The convergence process will be stopped as soon as the residual falls below the absolute tolerance.",
    )
    relative_tolerance: float | None = Field(
        validation_alias="relativeTolerance",
        serialization_alias="relativeTolerance",
        default=0.01,
        description="Choose the relative tolerance for the residual. The convergence process will be stopped as soon as the ratio of current to initial residual falls below the relative tolerance.",
    )
    preconditioner: OneOf_PCGSolverPreconditioner | None = Field(default=None)
