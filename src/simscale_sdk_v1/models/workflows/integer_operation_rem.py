from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class IntegerOperationRem(SimScaleModel):
    operand_a: Any | None = Field(
        validation_alias="operandA",
        serialization_alias="operandA",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    operand_b: Any | None = Field(
        validation_alias="operandB",
        serialization_alias="operandB",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    value_model_type: str
