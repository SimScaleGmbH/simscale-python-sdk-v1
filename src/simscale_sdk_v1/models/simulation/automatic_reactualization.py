from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AutomaticReactualization(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AUTOMATIC",
        description="Schema name: AutomaticReactualization",
    )
    max_num_iterations: int | None = Field(
        validation_alias="maxNumIterations", serialization_alias="maxNumIterations", default=10
    )
    iteration_criterion: float | None = Field(
        validation_alias="iterationCriterion", serialization_alias="iterationCriterion", default=0.05
    )
