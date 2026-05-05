from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__volume_custom_sizing_custom_sizing_modes import (
    OneOf_VolumeCustomSizingCustomSizingModes,
)
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class VolumeCustomSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VOLUME_CUSTOM_SIZING",
        description="Schema name: VolumeCustomSizing",
    )
    name: str | None = Field(default="Volume sizing")
    custom_sizing_modes: OneOf_VolumeCustomSizingCustomSizingModes | None = Field(
        validation_alias="customSizingModes", serialization_alias="customSizingModes", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
