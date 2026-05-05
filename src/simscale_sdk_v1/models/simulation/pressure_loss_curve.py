from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.directional_dependency import DirectionalDependency
from simscale_sdk_v1.models.simulation.one_of__pressure_loss_curve_porous_media_heat_transfer import (
    OneOf_PressureLossCurvePorousMediaHeatTransfer,
)
from simscale_sdk_v1.models.simulation.pressure_loss_data import PressureLossData
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PressureLossCurve(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE_LOSS_CURVE",
        description="Schema name: PressureLossCurve",
    )
    name: str | None = Field(default=None)
    pressure_loss_data: PressureLossData | None = Field(
        validation_alias="pressureLossData", serialization_alias="pressureLossData", default=None
    )
    directional_dependency: DirectionalDependency | None = Field(
        validation_alias="directionalDependency", serialization_alias="directionalDependency", default=None
    )
    porous_media_heat_transfer: OneOf_PressureLossCurvePorousMediaHeatTransfer | None = Field(
        validation_alias="porousMediaHeatTransfer", serialization_alias="porousMediaHeatTransfer", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
