from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__min_max_fields_calculation_result_control_item_field_selection import (
    OneOf_MinMaxFieldsCalculationResultControlItemFieldSelection,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class MinMaxFieldsCalculationResultControlItem(SimScaleModel):
    """Use Min-max to output the minimum and maximum nodal values of the selected result quantity on the assigned entity."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MIN_MAX_FIELDS_CALCULATION",
        description="Use Min-max to output the minimum and maximum nodal values of the selected result quantity on the assigned entity.  Schema name: MinMaxFieldsCalculationResultControlItem",
    )
    name: str | None = Field(default=None)
    coordinate_system: str | None = Field(
        validation_alias="coordinateSystem",
        serialization_alias="coordinateSystem",
        default=None,
        description="The coordinate system in which the components of the selected field will be computed. Select from the available local coordinate systems or create a new one (defaults to Global).Global — Vector components are defined along the global x, y, and z axes.Add new — Creates a new local coordinate system. The following types are available:Cartesian — Vector components are defined along the local e1, e2, and e3 axes.Cylindrical — Vector components are defined as radial (ur), tangential (uΦ), and axial (uz).",
    )
    field_selection: OneOf_MinMaxFieldsCalculationResultControlItemFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
