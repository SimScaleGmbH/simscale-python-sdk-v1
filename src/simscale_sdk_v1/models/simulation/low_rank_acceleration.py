from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class LowRankAcceleration(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LOW_RANK",
        description="Schema name: LowRankAcceleration",
    )
    low_rank_threshold: float | None = Field(
        validation_alias="lowRankThreshold", serialization_alias="lowRankThreshold", default=0.0
    )
