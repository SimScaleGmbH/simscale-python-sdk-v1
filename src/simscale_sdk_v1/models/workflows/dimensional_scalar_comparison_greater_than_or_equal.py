from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DimensionalScalarComparisonGreaterThanOrEqual(SimScaleModel):
    operand_a: Any | None = Field(
        validation_alias="operandA",
        serialization_alias="operandA",
        default=None,
        description="Value model for a dimensional scalar.  Resolves to an object node with field `value` (double node) and field `unit` (text node).  Note: during resolution all dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s).",
    )
    operand_b: Any | None = Field(
        validation_alias="operandB",
        serialization_alias="operandB",
        default=None,
        description="Value model for a dimensional scalar.  Resolves to an object node with field `value` (double node) and field `unit` (text node).  Note: during resolution all dimensionals are converted to base SI units (e.g. 50 miles/hour -> 22.352 m/s).",
    )
    value_model_type: str
