from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.refinement_level import RefinementLevel


class DistanceRegionRefinementWithLevels(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISTANCE",
        description="Schema name: DistanceRegionRefinementWithLevels",
    )
    distance_refinement_levels: list[RefinementLevel] | None = Field(
        validation_alias="distanceRefinementLevels",
        serialization_alias="distanceRefinementLevels",
        default=[{"distance": {"value": 1, "unit": "m"}, "level": 1}],
    )
