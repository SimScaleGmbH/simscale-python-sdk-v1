from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of_pbicg_solver_preconditioner import OneOf_PBICGSolverPreconditioner


class PBICGSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="PBICG", description="Schema name: PBICGSolver"
    )
    absolute_tolerance: float | None = Field(
        validation_alias="absoluteTolerance",
        serialization_alias="absoluteTolerance",
        default=1e-05,
        description="Define the absolute tolerance for the residual. The convergence process will be stopped as soon as the residual falls below the absolute tolerance.",
    )
    relative_tolerance: float | None = Field(
        validation_alias="relativeTolerance",
        serialization_alias="relativeTolerance",
        default=None,
        description="Choose the relative tolerance for the residual. The convergence process will be stopped as soon as the ratio of current to initial residual falls below the relative tolerance.",
    )
    preconditioner: OneOf_PBICGSolverPreconditioner | None = Field(default=None)
