from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_contact_result_control_item_contact_type import (
    OneOf_MarcContactResultControlItemContactType,
)


class MarcContactResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONTACT",
        description="Schema name: MarcContactResultControlItem",
    )
    name: str | None = Field(default=None)
    contact_type: OneOf_MarcContactResultControlItemContactType | None = Field(
        validation_alias="contactType", serialization_alias="contactType", default=None
    )
