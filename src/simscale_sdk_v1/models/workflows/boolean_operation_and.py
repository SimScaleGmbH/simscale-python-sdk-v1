from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class BooleanOperationAnd(SimScaleModel):
    operand_a: Any | None = Field(
        validation_alias="operandA",
        serialization_alias="operandA",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
    operand_b: Any | None = Field(
        validation_alias="operandB",
        serialization_alias="operandB",
        default=None,
        description="Value model of a boolean value. Resolves to a JSON boolean or null node.",
    )
