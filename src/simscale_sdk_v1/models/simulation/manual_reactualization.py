from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ManualReactualization(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL",
        description="Schema name: ManualReactualization",
    )
    num_iterations: int | None = Field(validation_alias="numIterations", serialization_alias="numIterations", default=2)
