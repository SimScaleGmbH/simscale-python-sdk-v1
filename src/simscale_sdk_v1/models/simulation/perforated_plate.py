from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__perforated_plate_porous_media_heat_transfer import (
    OneOf_PerforatedPlatePorousMediaHeatTransfer,
)
from simscale_sdk_v1.models.simulation.plate_data import PlateData
from simscale_sdk_v1.models.simulation.rectifying_darcy_forchheimer import RectifyingDarcyForchheimer
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PerforatedPlate(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PERFORATED_PLATE",
        description="Schema name: PerforatedPlate",
    )
    name: str | None = Field(default=None)
    plate_data: PlateData | None = Field(validation_alias="plateData", serialization_alias="plateData", default=None)
    darcy_forchheimer_type: RectifyingDarcyForchheimer | None = Field(
        validation_alias="darcyForchheimerType", serialization_alias="darcyForchheimerType", default=None
    )
    porous_media_heat_transfer: OneOf_PerforatedPlatePorousMediaHeatTransfer | None = Field(
        validation_alias="porousMediaHeatTransfer", serialization_alias="porousMediaHeatTransfer", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
