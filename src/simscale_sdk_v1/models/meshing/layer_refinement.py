from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class LayerRefinement(SimScaleModel):
    """Layer inflation allows the creation of prismatic boundary layers for certain mesh regions.Prismatic layers are mostly used in CFD simulations on no-slip walls in order to efficiently capture the boundary layer velocity profile, but they may be also used in certain structural simulations like stamping or deep-drawing processes. The figure shows a sample mesh with boundary layers added."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LAYER_INFLATION",
        description="Layer inflation allows the creation of prismatic boundary layers for certain mesh regions.Prismatic layers are mostly used in CFD simulations on no-slip walls in order to efficiently capture the boundary layer velocity profile, but they may be also used in certain structural simulations like stamping or deep-drawing processes. The figure shows a sample mesh with boundary layers added.  Schema name: LayerRefinement",
    )
    name: str | None = Field(default="Layer inflation")
    total_thickness: float | None = Field(
        validation_alias="totalThickness",
        serialization_alias="totalThickness",
        default=0.01,
        description="This parameter controls the overall thickness of all the generated boundary layers together. This value must be smaller than the minimal geometry thickness at the specified locations, otherwise the meshing will fail.",
    )
    layers: int | None = Field(
        default=5, description="The number of layers defines how many prismatic boundary layers should be created."
    )
    stretch_factor: float | None = Field(
        validation_alias="stretchFactor",
        serialization_alias="stretchFactor",
        default=1.3,
        description="The stretch factor determines how the boundary layers grow in thickness from the wall to the internal mesh. The larger the ratio, the larger each element layer will be in comparison to the neighbouring layer closer to the wall. The figure shows a ratio of 1.3.",
    )
    allow_quadrangles: bool | None = Field(
        validation_alias="allowQuadrangles",
        serialization_alias="allowQuadrangles",
        default=False,
        description="This parameter determines if quadrangular surface elements shall be allowed. When disabled, only triangles will be used. Meshing with triangles only is usually more robust while quadrangular elements may lead to better results. The figure shows sample meshes with quadrangular surface elements disallowed (left) and allowed (right).",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
