from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.real_value import RealValue


class RealOperationPlus(SimScaleModel):
    operand_a: RealValue | None = Field(validation_alias="operandA", serialization_alias="operandA", default=None)
    operand_b: Any | None = Field(
        validation_alias="operandB",
        serialization_alias="operandB",
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
