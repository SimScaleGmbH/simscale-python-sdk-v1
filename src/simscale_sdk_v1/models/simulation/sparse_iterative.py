from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SparseIterative(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPARSE_ITERATIVE",
        description="Schema name: SparseIterative",
    )
    preconditioner: Literal["DIAGONAL", "SCALED_DIAGONAL", "INCOMPLETE_CHOLESKY"] | None = Field(
        default="INCOMPLETE_CHOLESKY",
        description="Selects the preconditioning technique used to accelerate convergence of the iterative solver.Incomplete Cholesky: Recommended default. Provides the best convergence reduction at the cost of slightly higher setup time.Diagonal: Cheapest to compute but least effective. Suitable only for well-conditioned systems or when memory is very limited.Scaled Diagonal: Improves upon plain diagonal at minimal extra cost; useful when large stiffness contrasts exist between parts.",
    )
    non_convergence_action: Literal["STOP", "SWITCH_TO_DIRECT_SOLVER"] | None = Field(
        validation_alias="nonConvergenceAction",
        serialization_alias="nonConvergenceAction",
        default="SWITCH_TO_DIRECT_SOLVER",
        description="Defines what Marc should do if the iterative solver fails to converge within the allowed number of iterations for a given increment.Switch to Direct Solver: Automatically falls back to the direct solver for the failed increment and then resumes iterative solving for subsequent increments. This provides a safety net while still benefiting from the lower memory usage of the iterative solver in most increments.Stop: Terminates the analysis if the iterative solver does not converge. Use this when a fallback to the direct solver is not feasible due to memory constraints, or when you want strict control over solver behavior.",
    )
    convergence_tolerance: float | None = Field(
        validation_alias="convergenceTolerance",
        serialization_alias="convergenceTolerance",
        default=0.0001,
        description="The relative residual tolerance used to determine when the iterative solver has found a sufficiently accurate solution to the linear system within a single Newton-Raphson iteration. The solver stops when the norm of the residual is reduced below the fraction of the initial residual. A smaller value gives a more accurate linear solution but requires more iterations; the default of 10-4 is suitable for most nonlinear structural analyses.",
    )
