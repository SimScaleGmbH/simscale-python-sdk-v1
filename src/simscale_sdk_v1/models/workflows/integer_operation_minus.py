from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.integer_value import IntegerValue


class IntegerOperationMinus(SimScaleModel):
    operand_a: IntegerValue | None = Field(validation_alias="operandA", serialization_alias="operandA", default=None)
    operand_b: Any | None = Field(
        validation_alias="operandB",
        serialization_alias="operandB",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
