from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.stress_tensor__pressure import StressTensor_Pressure
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SubdomainStressInitialCondition(SimScaleModel):
    name: str | None = Field(default=None)
    subdomain_value: StressTensor_Pressure | None = Field(
        validation_alias="subdomainValue", serialization_alias="subdomainValue", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
