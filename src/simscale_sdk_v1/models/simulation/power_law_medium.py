from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__power_law_medium_porous_media_heat_transfer import (
    OneOf_PowerLawMediumPorousMediaHeatTransfer,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PowerLawMedium(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="POWER_LAW",
        description="Schema name: PowerLawMedium",
    )
    name: str | None = Field(default=None)
    linear_coefficient: float | None = Field(
        validation_alias="linearCoefficient", serialization_alias="linearCoefficient", default=1
    )
    exponent_coefficient: float | None = Field(
        validation_alias="exponentCoefficient", serialization_alias="exponentCoefficient", default=2
    )
    porous_media_heat_transfer: OneOf_PowerLawMediumPorousMediaHeatTransfer | None = Field(
        validation_alias="porousMediaHeatTransfer", serialization_alias="porousMediaHeatTransfer", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
