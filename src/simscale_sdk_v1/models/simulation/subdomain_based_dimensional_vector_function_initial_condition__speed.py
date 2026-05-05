from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector_function__speed import DimensionalVectorFunction_Speed
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SubdomainBasedDimensionalVectorFunctionInitialCondition_Speed(SimScaleModel):
    name: str | None = Field(default=None)
    subdomain_value: DimensionalVectorFunction_Speed | None = Field(
        validation_alias="subdomainValue", serialization_alias="subdomainValue", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
