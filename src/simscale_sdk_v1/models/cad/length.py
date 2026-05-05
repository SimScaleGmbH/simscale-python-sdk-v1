from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Length(SimScaleModel):
    """Length with unit."""

    value: float = Field(description="Length value.")
    unit: Literal["m", "cm", "mm", "yd", "ft", "in"] = Field(description="Unit of measurement.")
