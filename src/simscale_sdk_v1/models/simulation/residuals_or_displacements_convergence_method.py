from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__residuals_or_displacements_convergence_method_convergence_criteria import (
    OneOf_ResidualsOrDisplacementsConvergenceMethodConvergenceCriteria,
)


class ResidualsOrDisplacementsConvergenceMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RESIDUALS_OR_DISPLACEMENTS",
        description="Schema name: ResidualsOrDisplacementsConvergenceMethod",
    )
    convergence_criteria: OneOf_ResidualsOrDisplacementsConvergenceMethodConvergenceCriteria | None = Field(
        validation_alias="convergenceCriteria", serialization_alias="convergenceCriteria", default=None
    )
