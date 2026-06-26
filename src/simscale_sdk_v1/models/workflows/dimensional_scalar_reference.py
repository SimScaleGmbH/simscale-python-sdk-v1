from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.dimensional_scalar_object import DimensionalScalarObject
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class DimensionalScalarReference(SimScaleModel):
    default_value: DimensionalScalarObject | None = Field(
        validation_alias="defaultValue", serialization_alias="defaultValue", default=None
    )
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    value_model_type: str
