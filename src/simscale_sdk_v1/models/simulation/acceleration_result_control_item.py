from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.global_acceleration_type import GlobalAccelerationType


class AccelerationResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ACCELERATION",
        description="Schema name: AccelerationResultControlItem",
    )
    name: str | None = Field(default=None)
    acceleration_type: GlobalAccelerationType | None = Field(
        validation_alias="accelerationType", serialization_alias="accelerationType", default=None
    )
