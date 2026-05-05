from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.distance_sizing import DistanceSizing
from simscale_sdk_v1.models.meshing.one_of__distance_volume_custom_sizing_curvature import (
    OneOf_DistanceVolumeCustomSizingCurvature,
)


class DistanceVolumeCustomSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DISTANCE_CUSTOM_SIZING",
        description="Schema name: DistanceVolumeCustomSizing",
    )
    distance_sizing_values: list[DistanceSizing] | None = Field(
        validation_alias="distanceSizingValues",
        serialization_alias="distanceSizingValues",
        default=[{"distance": {"value": 0, "unit": "m"}, "length": {"value": 1, "unit": "m"}}],
        description="Define mesh element sizes inside and around the selected volumes. Each row specifies how the mesh size changes with the distance from the volume boundary: Distance [m] is the distance from the closest point on the boundary, Default size [m] is the target element size at that distance, and Min. size [m] is the smallest allowed element size. Distances must be specified in increasing order (e.g. d1 = 0 m, default = 1e-3 m, min = 5e-4 m; d2 = 0.5 m, default = 3e-3 m, min = 1e-3 m). When Distance = 0, the sizes apply inside the selected volume, and larger distances control how the mesh transitions outside it in all directions.",
    )
    curvature: OneOf_DistanceVolumeCustomSizingCurvature | None = Field(default=None)
