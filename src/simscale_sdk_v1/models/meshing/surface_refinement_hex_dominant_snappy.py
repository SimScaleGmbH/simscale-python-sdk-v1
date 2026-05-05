from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.meshing.one_of__surface_refinement_hex_dominant_snappy_cell_zone import (
    OneOf_SurfaceRefinementHexDominantSnappyCellZone,
)
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SurfaceRefinementHexDominantSnappy(SimScaleModel):
    """A surface refinement can be used to refine the mesh near the surfaces of assigned faces and/or solids. A surface refinement can also be used to create a cell zone."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_HEX_DOMINANT_SNAPPY_V3",
        description="A surface refinement can be used to refine the mesh near the surfaces of assigned faces and/or solids. A surface refinement can also be used to create a cell zone.  Schema name: SurfaceRefinementHexDominantSnappy",
    )
    name: str | None = Field(default="Surface refinement")
    min_length: Dimensional_Length | None = Field(
        validation_alias="minLength", serialization_alias="minLength", default=None
    )
    max_length: Dimensional_Length | None = Field(
        validation_alias="maxLength", serialization_alias="maxLength", default=None
    )
    cell_zone: OneOf_SurfaceRefinementHexDominantSnappyCellZone | None = Field(
        validation_alias="cellZone", serialization_alias="cellZone", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
