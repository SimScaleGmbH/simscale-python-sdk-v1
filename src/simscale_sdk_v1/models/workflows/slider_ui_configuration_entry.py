from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value_reference import ValueReference


class SliderUiConfigurationEntry(SimScaleModel):
    configuration_entry_type: str
    value_reference: ValueReference | None = Field(
        validation_alias="valueReference", serialization_alias="valueReference", default=None
    )
    maximum_value: Any | None = Field(
        validation_alias="maximumValue",
        serialization_alias="maximumValue",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    minimum_value: Any | None = Field(
        validation_alias="minimumValue",
        serialization_alias="minimumValue",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    step_size: Any | None = Field(
        validation_alias="stepSize",
        serialization_alias="stepSize",
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
