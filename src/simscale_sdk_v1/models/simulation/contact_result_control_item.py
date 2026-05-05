from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ContactResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CONTACT",
        description="Schema name: ContactResultControlItem",
    )
    name: str | None = Field(default=None)
    contact_type: Literal["PRESSURE", "RESULT"] | None = Field(
        validation_alias="contactType", serialization_alias="contactType", default="PRESSURE"
    )
