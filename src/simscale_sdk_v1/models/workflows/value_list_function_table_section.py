from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.value import Value


class ValueListFunctionTableSection(SimScaleModel):
    at: Any | None = Field(
        default=None,
        description="Value model for a dimensional scalar.  Resolves to an object node with field `value` (double node) and field `unit` (text node).  Note: during resolution dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s), unless the resolution context opts out of the conversion to keep the original units; results of operations are always in base SI units.",
    )
    element_model: Value | None = Field(
        validation_alias="elementModel", serialization_alias="elementModel", default=None
    )
    hold_above_range: Any | None = Field(
        validation_alias="holdAboveRange",
        serialization_alias="holdAboveRange",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
    hold_below_range: Any | None = Field(
        validation_alias="holdBelowRange",
        serialization_alias="holdBelowRange",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
    logarithmic: Any | None = Field(
        default=None, description="Value model of a boolean value. Resolves to a JSON boolean or null node."
    )
    parameter_column: str | None = Field(
        validation_alias="parameterColumn", serialization_alias="parameterColumn", default=None
    )
    quantity_column: str | None = Field(
        validation_alias="quantityColumn", serialization_alias="quantityColumn", default=None
    )
    stepwise: Any | None = Field(
        default=None, description="Value model of a boolean value. Resolves to a JSON boolean or null node."
    )
    value_list: Any | None = Field(
        validation_alias="valueList",
        serialization_alias="valueList",
        default=None,
        description="Value model for a list of values. Resolves to a JSON array.",
    )
    value_model_type: str
