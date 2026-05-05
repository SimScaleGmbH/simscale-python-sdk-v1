from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PressureDifferenceResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE_DIFFERENCE",
        description="Schema name: PressureDifferenceResultControl",
    )
    name: str | None = Field(default=None)
    absolute_value_of_pressure_difference: bool | None = Field(
        validation_alias="absoluteValueOfPressureDifference",
        serialization_alias="absoluteValueOfPressureDifference",
        default=True,
        description="Ensure a non-negative pressure difference result. Useful for many applications in which the pressure difference is assumed to be a pressure drop. However, leaving this on may yield non-physical results for some combinations of static/total pressure.",
    )
    inlet_face_pressure_difference_type: Literal["STATIC_PRESSURE", "TOTAL_PRESSURE"] | None = Field(
        validation_alias="inletFacePressureDifferenceType",
        serialization_alias="inletFacePressureDifferenceType",
        default="STATIC_PRESSURE",
        description="The total pressure is the sum of the static pressure and the dynamic pressure.",
    )
    inlet_face_topological_reference: TopologicalReference | None = Field(
        validation_alias="inletFaceTopologicalReference",
        serialization_alias="inletFaceTopologicalReference",
        default=None,
    )
    outlet_face_pressure_difference_type: Literal["STATIC_PRESSURE", "TOTAL_PRESSURE"] | None = Field(
        validation_alias="outletFacePressureDifferenceType",
        serialization_alias="outletFacePressureDifferenceType",
        default="STATIC_PRESSURE",
        description="The total pressure is the sum of the static pressure and the dynamic pressure.",
    )
    outlet_face_topological_reference: TopologicalReference | None = Field(
        validation_alias="outletFaceTopologicalReference",
        serialization_alias="outletFaceTopologicalReference",
        default=None,
    )
