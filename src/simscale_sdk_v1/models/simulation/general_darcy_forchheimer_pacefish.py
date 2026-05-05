from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__area import Dimensional_Area
from simscale_sdk_v1.models.simulation.one_of__general_darcy_forchheimer_pacefish_darcy_forchheimer_type import (
    OneOf_GeneralDarcyForchheimerPacefishDarcyForchheimerType,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class GeneralDarcyForchheimerPacefish(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="GENERAL_POROSITY",
        description="Schema name: GeneralDarcyForchheimerPacefish",
    )
    name: str | None = Field(default=None)
    darcy_forchheimer_type: OneOf_GeneralDarcyForchheimerPacefishDarcyForchheimerType | None = Field(
        validation_alias="darcyForchheimerType", serialization_alias="darcyForchheimerType", default=None
    )
    permeability: Dimensional_Area | None = Field(default=None)
    friction_form_coefficient: float | None = Field(
        validation_alias="frictionFormCoefficient",
        serialization_alias="frictionFormCoefficient",
        default=1.0,
        description="Friction form coefficient defines the pressure losses due to inertial effects through the porous object. The greater the friction form coefficient, the greater the pressure losses due to inertial effects  are. Friction form coefficient of zero means that there are no inertial losses through the porous object.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
