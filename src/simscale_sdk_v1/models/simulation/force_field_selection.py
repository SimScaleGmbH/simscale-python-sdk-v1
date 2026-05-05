from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__force_field_selection_force_type import (
    OneOf_ForceFieldSelectionForceType,
)


class ForceFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FORCE",
        description="Schema name: ForceFieldSelection",
    )
    force_type: OneOf_ForceFieldSelectionForceType | None = Field(
        validation_alias="forceType", serialization_alias="forceType", default=None
    )
