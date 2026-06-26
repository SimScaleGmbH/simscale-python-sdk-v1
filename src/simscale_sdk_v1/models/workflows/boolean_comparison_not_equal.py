from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.boolean_value import BooleanValue


class BooleanComparisonNotEqual(SimScaleModel):
    operand_a: BooleanValue | None = Field(validation_alias="operandA", serialization_alias="operandA", default=None)
    operand_b: BooleanValue | None = Field(validation_alias="operandB", serialization_alias="operandB", default=None)
    value_model_type: str
