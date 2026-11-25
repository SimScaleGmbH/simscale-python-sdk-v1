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
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the components of the selected field will be computed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Cylindrical — Vector components are defined as radial (ur), tangential (uΦ), and axial (uz).",
    )
    field_selection: OneOf_TemporalResponseResultControlItemFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
