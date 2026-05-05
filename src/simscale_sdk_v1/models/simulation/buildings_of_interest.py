from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class BuildingsOfInterest(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BUILDINGS_OF_INTEREST",
        description="Schema name: BuildingsOfInterest",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
