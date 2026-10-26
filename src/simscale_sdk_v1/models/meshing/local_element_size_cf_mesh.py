from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class LocalElementSizeCfMesh(SimScaleModel):
    """Surface custom sizing refines the mesh on the selected faces. The maximum edge length is the target cell size on the faces, the minimum element size is the lower bound for the automatic refinement of curvature and small features on them. Use it for faces of interest, for example inlets, outlets or walls with small details."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LOCAL_SIZING_CF_MESH",
        description="Surface custom sizing refines the mesh on the selected faces. The maximum edge length is the target cell size on the faces, the minimum element size is the lower bound for the automatic refinement of curvature and small features on them. Use it for faces of interest, for example inlets, outlets or walls with small details.  Schema name: LocalElementSizeCfMesh",
    )
    name: str | None = Field(default="Local element size")
    max_element_size: Dimensional_Length | None = Field(
        validation_alias="maxElementSize", serialization_alias="maxElementSize", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
