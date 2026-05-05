from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MeasureEntitiesParameters(SimScaleModel):
    unit: Literal["m", "cm", "mm", "yd", "ft", "in"] = Field(description="Unit of measurement.")
    entities: list[str] = Field(description="List of topological entities.")
