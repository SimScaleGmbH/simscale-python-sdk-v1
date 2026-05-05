from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_contact_force_field_selection_contact_type import (
    OneOf_MarcContactForceFieldSelectionContactType,
)


class MarcContactForceFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONTACT_FORCE",
        description="Schema name: MarcContactForceFieldSelection",
    )
    contact_type: OneOf_MarcContactForceFieldSelectionContactType | None = Field(
        validation_alias="contactType", serialization_alias="contactType", default=None
    )
