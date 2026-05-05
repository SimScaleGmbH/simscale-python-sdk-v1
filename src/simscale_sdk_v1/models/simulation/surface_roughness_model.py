from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__surface_roughness_model_surface_roughness_type import (
    OneOf_SurfaceRoughnessModelSurfaceRoughnessType,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SurfaceRoughnessModel(SimScaleModel):
    name: str | None = Field(default=None)
    surface_roughness_type: OneOf_SurfaceRoughnessModelSurfaceRoughnessType | None = Field(
        validation_alias="surfaceRoughnessType", serialization_alias="surfaceRoughnessType", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
