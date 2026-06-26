from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class IntegerFunctionAbs(SimScaleModel):
    argument: Any | None = Field(
        default=None, description="Value model for a 64-bit signed integer value. Resolves to a long JSON node."
    )
