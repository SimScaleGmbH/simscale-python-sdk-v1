from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.refinement_length import RefinementLength
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class FeatureRefinementHexDominantSnappy(SimScaleModel):
    """A feature refinement can be used to refine the geometry’s feature edges. All edges whose adjacent surface normals form an angle of less than 150° will be refined."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FEATURE_HEX_DOMINANT_SNAPPY",
        description="A feature refinement can be used to refine the geometry’s feature edges. All edges whose adjacent surface normals form an angle of less than 150° will be refined.  Schema name: FeatureRefinementHexDominantSnappy",
    )
    name: str | None = Field(default="Feature refinement")
    distance_refinement_lengths: list[RefinementLength] | None = Field(
        validation_alias="distanceRefinementLengths",
        serialization_alias="distanceRefinementLengths",
        default=[{"distance": {"value": 1, "unit": "m"}, "length": {"value": 1, "unit": "m"}}],
        description="Specify the desired target cell edge length based on the distance to the feature edges. The edge and surface mesh will then be refined up until the specified distance in all directions from the edges.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
