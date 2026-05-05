from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FixedPointFrictionNonLinearityResolution(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_POINT",
        description="Schema name: FixedPointFrictionNonLinearityResolution",
    )
    max_num_iteration: int | None = Field(
        validation_alias="maxNumIteration", serialization_alias="maxNumIteration", default=10
    )
    iteration_criterion: float | None = Field(
        validation_alias="iterationCriterion", serialization_alias="iterationCriterion", default=0.0001
    )
