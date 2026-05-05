from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TrueLineSearch(SimScaleModel):
    """Line search can be used to improve convergence for nonlinear calculations with the Newton method."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TRUE",
        description="Line search can be used to improve convergence for nonlinear calculations with the Newton method.  Schema name: TrueLineSearch",
    )
    method: Literal["SECANT", "MIXED"] | None = Field(
        default="SECANT",
        description="Choose the method of the line search algorithm. The Secant method is a simple one dimensional search algorithm. The mixed method is a more elaborate algorithm that uses variable bounds.",
    )
    residual: float | None = Field(default=0.001, description="Set the residual for the line search convergence")
    max_iterations: int | None = Field(
        validation_alias="maxIterations",
        serialization_alias="maxIterations",
        default=3,
        description="Set the maximum number for line search iterations. Typically a sinlge-digit number should be sufficient.",
    )
