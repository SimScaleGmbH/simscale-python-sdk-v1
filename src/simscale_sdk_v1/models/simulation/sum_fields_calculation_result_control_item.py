from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__sum_fields_calculation_result_control_item_field_selection import (
    OneOf_SumFieldsCalculationResultControlItemFieldSelection,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SumFieldsCalculationResultControlItem(SimScaleModel):
    """Use Sum to output the sum of the nodal values of the selected result quantity on the assigned entity. This option is only available for use with force solution fields and must be used when computing any force e.g. reaction force on a selected entity."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SUM_FIELDS_CALCULATION",
        description="Use Sum to output the sum of the nodal values of the selected result quantity on the assigned entity. This option is only available for use with force solution fields and must be used when computing any force e.g. reaction force on a selected entity.  Schema name: SumFieldsCalculationResultControlItem",
    )
    name: str | None = Field(default=None)
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the components of the selected field will be computed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Cylindrical — Vector components are defined as radial (ur), tangential (uΦ), and axial (uz).",
    )
    field_selection: OneOf_SumFieldsCalculationResultControlItemFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
