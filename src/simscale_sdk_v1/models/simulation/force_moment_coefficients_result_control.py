from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__area import Dimensional_Area
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional__speed import Dimensional_Speed
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.one_of__force_moment_coefficients_result_control_write_control import (
    OneOf_ForceMomentCoefficientsResultControlWriteControl,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ForceMomentCoefficientsResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FORCE_AND_MOMENT_COEFFICIENTS",
        description="Schema name: ForceMomentCoefficientsResultControl",
    )
    name: str | None = Field(default=None)
    center_of_rotation: DimensionalVector_Length | None = Field(
        validation_alias="centerOfRotation", serialization_alias="centerOfRotation", default=None
    )
    lift_direction: DimensionalVector_Length | None = Field(
        validation_alias="liftDirection", serialization_alias="liftDirection", default=None
    )
    drag_direction: DimensionalVector_Length | None = Field(
        validation_alias="dragDirection", serialization_alias="dragDirection", default=None
    )
    pitch_axis: DimensionalVector_Length | None = Field(
        validation_alias="pitchAxis", serialization_alias="pitchAxis", default=None
    )
    freestream_velocity_magnitude: Dimensional_Speed | None = Field(
        validation_alias="freestreamVelocityMagnitude", serialization_alias="freestreamVelocityMagnitude", default=None
    )
    reference_length: Dimensional_Length | None = Field(
        validation_alias="referenceLength", serialization_alias="referenceLength", default=None
    )
    reference_area_value: Dimensional_Area | None = Field(
        validation_alias="referenceAreaValue", serialization_alias="referenceAreaValue", default=None
    )
    write_control: OneOf_ForceMomentCoefficientsResultControlWriteControl | None = Field(
        validation_alias="writeControl", serialization_alias="writeControl", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
