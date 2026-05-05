from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.meshing.refinement_level import RefinementLevel


class FeatureRefinement(SimScaleModel):
    """A feature refinement can be used to refine the geometry’s feature edges. All edges whose adjacent surface normals form an angle of less than 150° will be refined."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FEATURE",
        description="A feature refinement can be used to refine the geometry’s feature edges. All edges whose adjacent surface normals form an angle of less than 150° will be refined.  Schema name: FeatureRefinement",
    )
    name: str | None = Field(default="Feature refinement")
    included_angle: Dimensional_Angle | None = Field(
        validation_alias="includedAngle", serialization_alias="includedAngle", default=None
    )
    distance_refinement_levels: list[RefinementLevel] | None = Field(
        validation_alias="distanceRefinementLevels",
        serialization_alias="distanceRefinementLevels",
        default=[{"distance": {"value": 1, "unit": "m"}, "level": 1}],
        description="This dynamic table allows you to add refinements to the mesh associated with the features (e.g. edges) in a specific distance to the features. Therefore specify the distance in the left box and the associated refinement level on the right (the higher, the finer). The pair (0,0) would mean that a refinement with level 0 would be introduced directly at the features of the mesh.",
    )
