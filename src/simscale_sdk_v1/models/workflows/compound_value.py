from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class CompoundValue(SimScaleModel):
    fields: dict[str, dict[str, Any]] | None = Field(default=None)
    polymorphic_compound_value: bool | None = Field(
        validation_alias="polymorphicCompoundValue", serialization_alias="polymorphicCompoundValue", default=None
    )
    subtype_id: str | None = Field(validation_alias="subtypeId", serialization_alias="subtypeId", default=None)
    subtypes: dict[str, Any] | None = Field(default=None)
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    value_model_type: str
