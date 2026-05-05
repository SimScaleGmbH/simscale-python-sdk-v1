from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__harmonic_displacement_result_control_item_harmonic_displacement_type import (
    OneOf_HarmonicDisplacementResultControlItemHarmonicDisplacementType,
)


class HarmonicDisplacementResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HARMONIC_DISPLACEMENT",
        description="Schema name: HarmonicDisplacementResultControlItem",
    )
    name: str | None = Field(default=None)
    harmonic_displacement_type: OneOf_HarmonicDisplacementResultControlItemHarmonicDisplacementType | None = Field(
        validation_alias="harmonicDisplacementType", serialization_alias="harmonicDisplacementType", default=None
    )
