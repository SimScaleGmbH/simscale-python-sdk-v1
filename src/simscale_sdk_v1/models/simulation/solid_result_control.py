from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__solid_result_control_area_calculation import (
    OneOf_SolidResultControlAreaCalculation,
)
from simscale_sdk_v1.models.simulation.one_of__solid_result_control_edge_calculation import (
    OneOf_SolidResultControlEdgeCalculation,
)
from simscale_sdk_v1.models.simulation.one_of__solid_result_control_point_data import OneOf_SolidResultControlPointData
from simscale_sdk_v1.models.simulation.one_of__solid_result_control_solution_fields import (
    OneOf_SolidResultControlSolutionFields,
)
from simscale_sdk_v1.models.simulation.one_of__solid_result_control_volume_calculation import (
    OneOf_SolidResultControlVolumeCalculation,
)


class SolidResultControl(SimScaleModel):
    solution_fields: list[OneOf_SolidResultControlSolutionFields] | None = Field(
        validation_alias="solutionFields",
        serialization_alias="solutionFields",
        default=None,
        description="Each mode is normalized using its largest component of displacement.",
    )
    edge_calculation: list[OneOf_SolidResultControlEdgeCalculation] | None = Field(
        validation_alias="edgeCalculation", serialization_alias="edgeCalculation", default=None
    )
    area_calculation: list[OneOf_SolidResultControlAreaCalculation] | None = Field(
        validation_alias="areaCalculation", serialization_alias="areaCalculation", default=None
    )
    volume_calculation: list[OneOf_SolidResultControlVolumeCalculation] | None = Field(
        validation_alias="volumeCalculation", serialization_alias="volumeCalculation", default=None
    )
    point_data: list[OneOf_SolidResultControlPointData] | None = Field(
        validation_alias="pointData", serialization_alias="pointData", default=None
    )
