from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fraction_value_initial_condition import FractionValueInitialCondition
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SubdomainFractionValueInitialCondition(SimScaleModel):
    name: str | None = Field(default=None)
    mass_fractions: list[FractionValueInitialCondition] | None = Field(
        validation_alias="massFractions", serialization_alias="massFractions", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
