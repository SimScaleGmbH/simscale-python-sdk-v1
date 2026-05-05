from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__temporal_response_result_control_item_field_selection import (
    OneOf_TemporalResponseResultControlItemFieldSelection,
)


class TemporalResponseResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TEMPORAL_RESPONSE",
        description="Schema name: TemporalResponseResultControlItem",
    )
    name: str | None = Field(default=None)
    field_selection: OneOf_TemporalResponseResultControlItemFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
