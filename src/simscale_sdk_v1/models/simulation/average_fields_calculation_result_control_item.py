from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__average_fields_calculation_result_control_item_field_selection import (
    OneOf_AverageFieldsCalculationResultControlItemFieldSelection,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class AverageFieldsCalculationResultControlItem(SimScaleModel):
    """Use Average to output the mean nodal value of the selected result quantity on the assigned entity. Note that this is not an area weighted average and that the nodal values from large elements will have the same contribution as those from small elements meaning that results can be misleading when mesh size varies on the selected entity."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AVERAGE_FIELDS_CALCULATION",
        description="Use Average to output the mean nodal value of the selected result quantity on the assigned entity. Note that this is not an area weighted average and that the nodal values from large elements will have the same contribution as those from small elements meaning that results can be misleading when mesh size varies on the selected entity.  Schema name: AverageFieldsCalculationResultControlItem",
    )
    name: str | None = Field(default=None)
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the components of the selected field will be computed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Cylindrical — Vector components are defined as radial (ur), tangential (uΦ), and axial (uz).",
    )
    field_selection: OneOf_AverageFieldsCalculationResultControlItemFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
