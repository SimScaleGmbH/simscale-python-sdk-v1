from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__simmetrix_boundary_layer_refinement_layer_type import (
    OneOf_SimmetrixBoundaryLayerRefinementLayerType,
)
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SimmetrixBoundaryLayerRefinement(SimScaleModel):
    """Layer inflation allows the creation of prismatic boundary layers for certain mesh regions.Prismatic layers are mostly used in CFD simulations on no-slip walls in order to efficiently capture the boundary layer velocity profile, but they may be also used in certain structural simulations like stamping or deep-drawing processes. The figure shows a sample mesh with boundary layers added."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMMETRIX_BOUNDARY_LAYER_V13",
        description="Layer inflation allows the creation of prismatic boundary layers for certain mesh regions.Prismatic layers are mostly used in CFD simulations on no-slip walls in order to efficiently capture the boundary layer velocity profile, but they may be also used in certain structural simulations like stamping or deep-drawing processes. The figure shows a sample mesh with boundary layers added.  Schema name: SimmetrixBoundaryLayerRefinement",
    )
    name: str | None = Field(default="Inflate boundary layer")
    layer_type: OneOf_SimmetrixBoundaryLayerRefinementLayerType | None = Field(
        validation_alias="layerType", serialization_alias="layerType", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
