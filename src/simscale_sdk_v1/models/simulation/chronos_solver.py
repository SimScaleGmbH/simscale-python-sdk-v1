from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_chronos_settings import AdvancedChronosSettings


class ChronosSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="CHRONOS", description="Schema name: ChronosSolver"
    )
    convergence_threshold: float | None = Field(
        validation_alias="convergenceThreshold",
        serialization_alias="convergenceThreshold",
        default=1e-06,
        description="Select the convergence tolerance. Can be smaller than with PETSc, and has a big impact on the newton convergence. It is recommended to start with a smaller value in case of convergence problems e.g. 1e-8 - 1e-10.",
    )
    max_iterations: int | None = Field(
        validation_alias="maxIterations",
        serialization_alias="maxIterations",
        default=1000,
        description="Maximum number of iterations for Chronos. Should be 1000 for AMG (max 3000), and 5000 with FSAI (max 10000).",
    )
    non_convergence_action: Literal["STOP", "SWITCH_TO_DIRECT_SOLVER"] | None = Field(
        validation_alias="nonConvergenceAction",
        serialization_alias="nonConvergenceAction",
        default="SWITCH_TO_DIRECT_SOLVER",
        description="Choose what happens if the linear solution with Chronos fails. Either stop the simulation, or rerun it with a direct solver (MUMPS)",
    )
    advanced_settings: AdvancedChronosSettings | None = Field(
        validation_alias="advancedSettings", serialization_alias="advancedSettings", default=None
    )
