from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ElementTechnologyDefinition(SimScaleModel):
    name: str | None = Field(default=None)
    reduced_integration: bool | None = Field(
        validation_alias="reducedIntegration", serialization_alias="reducedIntegration", default=False
    )
    lumped_mass: bool | None = Field(validation_alias="lumpedMass", serialization_alias="lumpedMass", default=False)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
