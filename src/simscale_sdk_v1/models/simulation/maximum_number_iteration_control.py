from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MaximumNumberIterationControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MAXIMUM_NUMBER",
        description="Schema name: MaximumNumberIterationControl",
    )
    max_num_iteration: int | None = Field(
        validation_alias="maxNumIteration", serialization_alias="maxNumIteration", default=30
    )
