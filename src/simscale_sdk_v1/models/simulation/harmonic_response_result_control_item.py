from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__harmonic_response_result_control_item_field_selection import (
    OneOf_HarmonicResponseResultControlItemFieldSelection,
)


class HarmonicResponseResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HARMONIC_RESPONSE",
        description="Schema name: HarmonicResponseResultControlItem",
    )
    name: str | None = Field(default=None)
    field_selection: OneOf_HarmonicResponseResultControlItemFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    complex_number: Literal["REAL_AND_IMAGINARY", "MAGNITUDE_AND_PHASE"] | None = Field(
        validation_alias="complexNumber", serialization_alias="complexNumber", default="REAL_AND_IMAGINARY"
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
