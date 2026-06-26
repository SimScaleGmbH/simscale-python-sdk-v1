from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class PairBooleanValueIntegerValue(SimScaleModel):
    first: Any | None = Field(
        default=None, description="Value model of a boolean value. Resolves to a JSON boolean or null node."
    )
    second: Any | None = Field(
        default=None, description="Value model for a 64-bit signed integer value. Resolves to a long JSON node."
    )
