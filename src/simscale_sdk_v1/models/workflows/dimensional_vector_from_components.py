from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DimensionalVectorFromComponents(SimScaleModel):
    unit: Any | None = Field(
        default=None, description="Value model for a measurement unit value. Resolves to a text JSON node."
    )
    x: Any | None = Field(
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
    y: Any | None = Field(
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
    z: Any | None = Field(
        default=None,
        description="Value model for a 64-bit double precision floating point number. Resolves to a double JSON node.",
    )
    value_model_type: str
