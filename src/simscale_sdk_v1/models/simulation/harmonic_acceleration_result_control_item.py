from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__harmonic_acceleration_result_control_item_harmonic_acceleration_type import (
    OneOf_HarmonicAccelerationResultControlItemHarmonicAccelerationType,
)


class HarmonicAccelerationResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HARMONIC_ACCELERATION",
        description="Schema name: HarmonicAccelerationResultControlItem",
    )
    name: str | None = Field(default=None)
    harmonic_acceleration_type: OneOf_HarmonicAccelerationResultControlItemHarmonicAccelerationType | None = Field(
        validation_alias="harmonicAccelerationType", serialization_alias="harmonicAccelerationType", default=None
    )
