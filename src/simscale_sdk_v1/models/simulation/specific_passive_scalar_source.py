from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__volumetric_passive_scalar_source_rate import (
    Dimensional_VolumetricPassiveScalarSourceRate,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SpecificPassiveScalarSource(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIFIC",
        description="Schema name: SpecificPassiveScalarSource",
    )
    name: str | None = Field(default=None)
    passive_scalar_variable: str | None = Field(
        validation_alias="passiveScalarVariable",
        serialization_alias="passiveScalarVariable",
        default="passive_scalar_one",
    )
    flux: Dimensional_VolumetricPassiveScalarSourceRate | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
