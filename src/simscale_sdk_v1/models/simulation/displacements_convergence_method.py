from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__displacements_convergence_method_convergence_criteria import (
    OneOf_DisplacementsConvergenceMethodConvergenceCriteria,
)


class DisplacementsConvergenceMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISPLACEMENTS",
        description="Schema name: DisplacementsConvergenceMethod",
    )
    convergence_criteria: OneOf_DisplacementsConvergenceMethodConvergenceCriteria | None = Field(
        validation_alias="convergenceCriteria", serialization_alias="convergenceCriteria", default=None
    )
