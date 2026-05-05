from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SmoothSolver(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="SMOOTH", description="Schema name: SmoothSolver"
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
    smoother: Literal["GAUSSSEIDEL", "SYMGAUSSSEIDEL", "DIC"] | None = Field(
        default="GAUSSSEIDEL", description="Choose a smoother for your solver."
    )
    num_sweeps: int | None = Field(
        validation_alias="numSweeps",
        serialization_alias="numSweeps",
        default=1,
        description="Define the numbers of sweeps.",
    )
