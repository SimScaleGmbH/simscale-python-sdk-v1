from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector_function__speed import DimensionalVectorFunction_Speed
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PredefinedTranslationalMotion(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PREDEFINED_TRANSLATIONAL_MOTION",
        description="Schema name: PredefinedTranslationalMotion",
    )
    name: str | None = Field(default=None)
    velocity: DimensionalVectorFunction_Speed | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
