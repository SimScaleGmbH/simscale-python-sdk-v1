from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RealFunctionMin(SimScaleModel):
    argument1: Any | None = Field(
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
    argument2: Any | None = Field(
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
    value_model_type: str
