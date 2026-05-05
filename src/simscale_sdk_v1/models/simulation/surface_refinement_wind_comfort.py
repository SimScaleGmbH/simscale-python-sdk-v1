from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__surface_refinement_wind_comfort_new_fineness import (
    OneOf_SurfaceRefinementWindComfortNewFineness,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SurfaceRefinementWindComfort(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_REFINEMENT_WIND_COMFORT",
        description="Schema name: SurfaceRefinementWindComfort",
    )
    name: str | None = Field(default="Surface refinement")
    new_fineness: OneOf_SurfaceRefinementWindComfortNewFineness | None = Field(
        validation_alias="newFineness", serialization_alias="newFineness", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
