from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__residuals_convergence_method_convergence_criteria import (
    OneOf_ResidualsConvergenceMethodConvergenceCriteria,
)


class ResidualsConvergenceMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RESIDUALS",
        description="Schema name: ResidualsConvergenceMethod",
    )
    convergence_criteria: OneOf_ResidualsConvergenceMethodConvergenceCriteria | None = Field(
        validation_alias="convergenceCriteria", serialization_alias="convergenceCriteria", default=None
    )
