from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Tolerance(SimScaleModel):
    absolute_tolerance: float | None = Field(
        validation_alias="absoluteTolerance",
        serialization_alias="absoluteTolerance",
        default=1e-05,
        description="Absolute tolerance is the measure of residual in the solution after the current iteration is solved. The solution is stopped when the absolute residual falls below this value.",
    )
    relative_tolerance: float | None = Field(
        validation_alias="relativeTolerance",
        serialization_alias="relativeTolerance",
        default=0.01,
        description="Relative tolerance is the ratio of current residual to the initial residual. The solution is stopped when the relative residual falls below this value.",
    )
