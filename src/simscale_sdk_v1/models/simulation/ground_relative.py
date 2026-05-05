from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class GroundRelative(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GROUND_RELATIVE",
        description="Schema name: GroundRelative",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
