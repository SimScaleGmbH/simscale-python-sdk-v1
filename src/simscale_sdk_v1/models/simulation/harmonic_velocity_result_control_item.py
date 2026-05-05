from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__harmonic_velocity_result_control_item_harmonic_velocity_type import (
    OneOf_HarmonicVelocityResultControlItemHarmonicVelocityType,
)


class HarmonicVelocityResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HARMONIC_VELOCITY",
        description="Schema name: HarmonicVelocityResultControlItem",
    )
    name: str | None = Field(default=None)
    harmonic_velocity_type: OneOf_HarmonicVelocityResultControlItemHarmonicVelocityType | None = Field(
        validation_alias="harmonicVelocityType", serialization_alias="harmonicVelocityType", default=None
    )
