from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__prandtl_les_delta_delta_coefficient import (
    OneOf_PrandtlLesDeltaDeltaCoefficient,
)


class PrandtlLesDelta(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRANDTL",
        description="Schema name: PrandtlLesDelta",
    )
    delta_coefficient: OneOf_PrandtlLesDeltaDeltaCoefficient | None = Field(
        validation_alias="deltaCoefficient", serialization_alias="deltaCoefficient", default=None
    )
    delta_reduction_coefficient: float | None = Field(
        validation_alias="deltaReductionCoefficient", serialization_alias="deltaReductionCoefficient", default=0.158
    )
