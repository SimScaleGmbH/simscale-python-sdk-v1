from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__electromagnetic_result_control_probe_point_field_selection import (
    OneOf_ElectromagneticResultControlProbePointFieldSelection,
)


class ElectromagneticResultControlProbePoint(SimScaleModel):
    name: str | None = Field(default=None)
    field_selection: OneOf_ElectromagneticResultControlProbePointFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
