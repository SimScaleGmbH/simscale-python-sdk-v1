from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ManualReynoldsScaling(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL_REYNOLDS_SCALING",
        description="Schema name: ManualReynoldsScaling",
    )
    reynolds_scaling_factor: float | None = Field(
        validation_alias="reynoldsScalingFactor", serialization_alias="reynoldsScalingFactor", default=1.0
    )
