from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__surface_custom_sizing_sizing import OneOf_SurfaceCustomSizingSizing
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SurfaceCustomSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_CUSTOM_SIZING",
        description="Schema name: SurfaceCustomSizing",
    )
    name: str | None = Field(default="Surface sizing")
    sizing: OneOf_SurfaceCustomSizingSizing | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
