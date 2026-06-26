from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.integer_value import IntegerValue


class IntegerFunctionMax(SimScaleModel):
    argument1: IntegerValue | None = Field(default=None)
    argument2: Any | None = Field(
        default=None, description="Value model for a 64-bit signed integer value. Resolves to a long JSON node."
    )
