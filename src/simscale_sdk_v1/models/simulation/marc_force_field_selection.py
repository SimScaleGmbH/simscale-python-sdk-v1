from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_force_field_selection_force_type import (
    OneOf_MarcForceFieldSelectionForceType,
)


class MarcForceFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FORCE",
        description="Schema name: MarcForceFieldSelection",
    )
    force_type: OneOf_MarcForceFieldSelectionForceType | None = Field(
        validation_alias="forceType", serialization_alias="forceType", default=None
    )
