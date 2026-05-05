from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelativeConvergenceCriteria(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE",
        description="Schema name: RelativeConvergenceCriteria",
    )
    tolerance: float | None = Field(
        default=5e-05,
        description="Set the threshold value for the relative convergence criterion. With this criterion, the solver considers a time step as converged if the maximum relative residual -- the maximum absolute residual divided by external loads and support reactions -- in a Newton iteration falls below the given value.Important remarks: This value is a compromise between solution time and accuracy. A larger value leads to a faster solution time at the cost of losing accuracy in each Newton iteration and possibly causing convergence problems in the following steps. We recommend an upper limit of 1-3.",
    )
