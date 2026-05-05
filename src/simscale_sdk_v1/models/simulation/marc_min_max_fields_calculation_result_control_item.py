from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__marc_min_max_fields_calculation_result_control_item_field_selection import (
    OneOf_MarcMinMaxFieldsCalculationResultControlItemFieldSelection,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class MarcMinMaxFieldsCalculationResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MIN_MAX_FIELDS_CALCULATION",
        description="Schema name: MarcMinMaxFieldsCalculationResultControlItem",
    )
    name: str | None = Field(default=None)
    field_selection: OneOf_MarcMinMaxFieldsCalculationResultControlItemFieldSelection | None = Field(
        validation_alias="fieldSelection", serialization_alias="fieldSelection", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
