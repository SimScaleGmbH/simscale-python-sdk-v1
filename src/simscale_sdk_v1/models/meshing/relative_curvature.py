from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelativeCurvature(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="RELATIVE_CURVATURE",
        description="Schema name: RelativeCurvature",
    )
    relative_curvature: float | None = Field(
        validation_alias="relativeCurvature",
        serialization_alias="relativeCurvature",
        default=None,
        description="The Number of nodes in a circle defines the relative chordal error on curved features in terms of number of mesh nodes in a full circle. The relative chordal error is the distance between the mesh element edge and the CAD model feature it represents divided by the mesh edge length.",
    )
