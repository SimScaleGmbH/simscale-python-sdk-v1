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
    enable_grading: bool | None = Field(
        validation_alias="enableGrading",
        serialization_alias="enableGrading",
        default=False,
        description="Enables the grading of the extrusion elements, starting from either side of the extrusion. The first layer has to be the smallest. The growth rate must be greater than 1. The elements stop growing once they reach the value defined through Thickness or Number of elements",
    )
    first_element_thickness: Dimensional_Length | None = Field(
        validation_alias="firstElementThickness", serialization_alias="firstElementThickness", default=None
    )
    growth_rate: float | None = Field(
        validation_alias="growthRate",
        serialization_alias="growthRate",
        default=1.2,
        description="The Growth rate defines the thickness ratio between adjacent boundary layer cells. It needs to be always greater than 1 such that the layer thickness increases towards the interior of the mesh. For the same number of layers and overall thickness the larger the growth rate is inversely proportional to the first cell thickness. Example of each cell being 1.5 times thicker than its adjacent.",
    )
    grading_side: Literal["START_FACE", "END_FACE", "BOTH"] | None = Field(
        validation_alias="gradingSide",
        serialization_alias="gradingSide",
        default="BOTH",
        description="Side defines which side of the extrusion will have the specified First layer thickness. The options are Start face, End face and Both.",
    )
    source_topological_reference: TopologicalReference | None = Field(
        validation_alias="sourceTopologicalReference", serialization_alias="sourceTopologicalReference", default=None
    )
    destination_topological_reference: TopologicalReference | None = Field(
        validation_alias="destinationTopologicalReference",
        serialization_alias="destinationTopologicalReference",
        default=None,
    )
