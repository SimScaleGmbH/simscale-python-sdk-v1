from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.one_of__pressure_loss_function_medium_porous_material_type import (
    OneOf_PressureLossFunctionMediumPorousMaterialType,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PressureLossFunctionMedium(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE_LOSS_FUNCTION",
        description="Schema name: PressureLossFunctionMedium",
    )
    name: str | None = Field(default=None)
    pressure_loss_function: DimensionalFunction_Pressure | None = Field(
        validation_alias="pressureLossFunction", serialization_alias="pressureLossFunction", default=None
    )
    porous_material_type: OneOf_PressureLossFunctionMediumPorousMaterialType | None = Field(
        validation_alias="porousMaterialType", serialization_alias="porousMaterialType", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
