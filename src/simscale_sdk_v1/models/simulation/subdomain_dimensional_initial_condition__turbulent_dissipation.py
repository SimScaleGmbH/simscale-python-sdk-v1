from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__turbulent_dissipation import Dimensional_TurbulentDissipation
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SubdomainDimensionalInitialCondition_TurbulentDissipation(SimScaleModel):
    name: str | None = Field(default=None)
    subdomain_value: Dimensional_TurbulentDissipation | None = Field(
        validation_alias="subdomainValue", serialization_alias="subdomainValue", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
