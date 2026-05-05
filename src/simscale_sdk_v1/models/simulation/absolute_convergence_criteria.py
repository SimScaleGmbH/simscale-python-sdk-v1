from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AbsoluteConvergenceCriteria(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ABSOLUTE",
        description="Schema name: AbsoluteConvergenceCriteria",
    )
    tolerance: float | None = Field(
        default=None,
        description="Set the threshold value for the absolute convergence criterion (measured in Newtons). With this criterion, the solver considers a time step as converged if the maximum absolute residual in a Newton iteration falls below the given value.Important remarks: This value is a compromise between solution time and accuracy. A larger value leads to a faster solution time at the cost of losing accuracy in each Newton iteration and possibly causing convergence problems in the following steps.",
    )
