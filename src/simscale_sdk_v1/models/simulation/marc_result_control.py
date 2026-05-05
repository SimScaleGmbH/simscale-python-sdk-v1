from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.marc_connector_point_data_item import MarcConnectorPointDataItem
from simscale_sdk_v1.models.simulation.one_of__marc_result_control_area_calculation import (
    OneOf_MarcResultControlAreaCalculation,
)
from simscale_sdk_v1.models.simulation.one_of__marc_result_control_solution_fields import (
    OneOf_MarcResultControlSolutionFields,
)
from simscale_sdk_v1.models.simulation.one_of__marc_result_control_volume_calculation import (
    OneOf_MarcResultControlVolumeCalculation,
)


class MarcResultControl(SimScaleModel):
    solution_fields: list[OneOf_MarcResultControlSolutionFields] | None = Field(
        validation_alias="solutionFields", serialization_alias="solutionFields", default=None
    )
    area_calculation: list[OneOf_MarcResultControlAreaCalculation] | None = Field(
        validation_alias="areaCalculation",
        serialization_alias="areaCalculation",
        default=None,
        description='Min-max: Identifies and records the absolute minimum and maximum values of the selected field within the designated area or volume.Average: Calculates the nodal average of the selected field across the entity. This can provide a representative mean value if the mesh is uniformly distributed, but might be skewed for meshes with highly varying element sizes, as the average is not area- or volume-weighted.Sum: Calculates the sum of the nodal field values across all nodes of the assigned area or volume; for example, summing "contact body force" returns the total contact force acting on the assigned body.',
    )
    volume_calculation: list[OneOf_MarcResultControlVolumeCalculation] | None = Field(
        validation_alias="volumeCalculation",
        serialization_alias="volumeCalculation",
        default=None,
        description='Min-max: Identifies and records the absolute minimum and maximum values of the selected field within the designated area or volume.Average: Calculates the nodal average of the selected field across the entity. This can provide a representative mean value if the mesh is uniformly distributed, but might be skewed for meshes with highly varying element sizes, as the average is not area- or volume-weighted.Sum: Calculates the sum of the nodal field values across all nodes of the assigned area or volume; for example, summing "contact body force" returns the total contact force acting on the assigned body.',
    )
    connector_point_data: list[MarcConnectorPointDataItem] | None = Field(
        validation_alias="connectorPointData", serialization_alias="connectorPointData", default=None
    )
