from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.one_of__moment_field_selection_moment_type import (
    OneOf_MomentFieldSelectionMomentType,
)


class MomentFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MOMENT",
        description="Schema name: MomentFieldSelection",
    )
    moment_type: OneOf_MomentFieldSelectionMomentType | None = Field(
        validation_alias="momentType", serialization_alias="momentType", default=None
    )
    reference_point: DimensionalVector_Length | None = Field(
        validation_alias="referencePoint", serialization_alias="referencePoint", default=None
    )
