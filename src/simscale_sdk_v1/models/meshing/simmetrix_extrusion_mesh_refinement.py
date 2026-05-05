from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.meshing.one_of__simmetrix_extrusion_mesh_refinement_sizing_type import (
    OneOf_SimmetrixExtrusionMeshRefinementSizingType,
)
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SimmetrixExtrusionMeshRefinement(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMMETRIX_EXTRUSION_MESH_REFINEMENT",
        description="Schema name: SimmetrixExtrusionMeshRefinement",
    )
    name: str | None = Field(default="Extrusion meshing refinement")
    sizing_type: OneOf_SimmetrixExtrusionMeshRefinementSizingType | None = Field(
        validation_alias="sizingType", serialization_alias="sizingType", default=None
    )
    surface_element_type: Literal["TRIANGULAR", "QUADDOMINANT"] | None = Field(
        validation_alias="surfaceElementType", serialization_alias="surfaceElementType", default="TRIANGULAR"
    )
    specify_local_size: bool | None = Field(
        validation_alias="specifyLocalSize", serialization_alias="specifyLocalSize", default=False
    )
    max_element_size: Dimensional_Length | None = Field(
        validation_alias="maxElementSize", serialization_alias="maxElementSize", default=None
    )
    source_topological_reference: TopologicalReference | None = Field(
        validation_alias="sourceTopologicalReference", serialization_alias="sourceTopologicalReference", default=None
    )
    destination_topological_reference: TopologicalReference | None = Field(
        validation_alias="destinationTopologicalReference",
        serialization_alias="destinationTopologicalReference",
        default=None,
    )
