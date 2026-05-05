from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_stress_field_selection_stress_type import (
    OneOf_MarcStressFieldSelectionStressType,
)


class MarcStressFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRESS",
        description="Schema name: MarcStressFieldSelection",
    )
    stress_type: OneOf_MarcStressFieldSelectionStressType | None = Field(
        validation_alias="stressType", serialization_alias="stressType", default=None
    )
