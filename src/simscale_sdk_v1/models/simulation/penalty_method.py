from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__penalty_method_contact_stiffness import (
    OneOf_PenaltyMethodContactStiffness,
)


class PenaltyMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PENALTY_METHOD",
        description="Schema name: PenaltyMethod",
    )
    contact_stiffness: OneOf_PenaltyMethodContactStiffness | None = Field(
        validation_alias="contactStiffness", serialization_alias="contactStiffness", default=None
    )
