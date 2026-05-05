from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.meshing.one_of__simmetrix_local_sizing_refinement_curvature import (
    OneOf_SimmetrixLocalSizingRefinementCurvature,
)
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SimmetrixLocalSizingRefinement(SimScaleModel):
    """Refine specific faces of interest or complex geometrical shapes by defining a local element size. This will ensure a relatively uniform mesh."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMMETRIX_LOCAL_SIZING_V10",
        description="Refine specific faces of interest or complex geometrical shapes by defining a local element size. This will ensure a relatively uniform mesh.  Schema name: SimmetrixLocalSizingRefinement",
    )
    name: str | None = Field(default="Local element size")
    max_element_size: Dimensional_Length | None = Field(
        validation_alias="maxElementSize", serialization_alias="maxElementSize", default=None
    )
    curvature: OneOf_SimmetrixLocalSizingRefinementCurvature | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
