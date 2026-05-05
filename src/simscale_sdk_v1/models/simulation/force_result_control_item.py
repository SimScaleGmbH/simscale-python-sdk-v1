from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__force_result_control_item_force_type import (
    OneOf_ForceResultControlItemForceType,
)


class ForceResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FORCE",
        description="Schema name: ForceResultControlItem",
    )
    name: str | None = Field(default=None)
    force_type: OneOf_ForceResultControlItemForceType | None = Field(
        validation_alias="forceType", serialization_alias="forceType", default=None
    )
