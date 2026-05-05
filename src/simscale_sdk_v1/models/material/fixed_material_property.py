from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.material.property_data_type import PropertyDataType


class FixedMaterialProperty(SimScaleModel):
    """A material property that has a fixed (constant) value."""

    name: str | None = Field(default=None, description="The material property name")
    label: str | None = Field(
        default=None,
        description="The material property label to support internationalization. The content of this field is a i18n key. If this field is not present, the name field can be used as a fallback for English language.",
    )
    unit: str | None = Field(default=None, description="The material property unit")
    value_type: str = Field(validation_alias="valueType", serialization_alias="valueType", default="fixed")
    data_type: PropertyDataType | None = Field(
        validation_alias="dataType", serialization_alias="dataType", default=None
    )
    value: Any = Field(description="The property value")
