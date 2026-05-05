from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__length import DimensionalVector_Length
from simscale_sdk_v1.models.simulation.one_of__forces_moments_result_control_write_control import (
    OneOf_ForcesMomentsResultControlWriteControl,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ForcesMomentsResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FORCES_AND_MOMENTS",
        description="Schema name: ForcesMomentsResultControl",
    )
    name: str | None = Field(default=None)
    center_of_rotation: DimensionalVector_Length | None = Field(
        validation_alias="centerOfRotation", serialization_alias="centerOfRotation", default=None
    )
    write_control: OneOf_ForcesMomentsResultControlWriteControl | None = Field(
        validation_alias="writeControl", serialization_alias="writeControl", default=None
    )
    fraction_from_end: float | None = Field(
        validation_alias="fractionFromEnd",
        serialization_alias="fractionFromEnd",
        default=0.2,
        description="It defines the point in simulation where the result output data extraction starts. For instance, Fraction from end of 1 (100%) extracts all data from the beginning of the simulation while default 0.2 extracts 20% data from the end of the simulation.",
    )
    export_statistics: bool | None = Field(
        validation_alias="exportStatistics",
        serialization_alias="exportStatistics",
        default=True,
        description="When this switch is activated, statistical data for the selected forces and moments will be exported:Minimum (MIN)Maximum (MAX)Average (AVG)Standard deviation (STDDEV)Root mean square (RMS)",
    )
    group_assignments: bool | None = Field(
        validation_alias="groupAssignments",
        serialization_alias="groupAssignments",
        default=True,
        description="When this switch is activated, forces and moments will be calculated cumulatively on all assignments. When deactivated, they will be calculated individually for each assignment.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
