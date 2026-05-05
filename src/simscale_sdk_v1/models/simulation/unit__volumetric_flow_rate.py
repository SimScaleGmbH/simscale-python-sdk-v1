from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Unit_VolumetricFlowRate(SimScaleModel):
    value: float | None = Field(default=None)
    unit: (
        Literal[
            "m³/s",
            "in³/s",
            "m³/min",
            "m³/h",
            "mm³/s",
            "mm³/min",
            "mm³/h",
            "cm³/s",
            "cm³/min",
            "cm³/h",
            "l/s",
            "l/min",
            "l/h",
            "in³/min",
            "in³/h",
            "ft³/s",
            "ft³/min",
            "ft³/h",
            "gal/min",
            "gal/h",
            "gal/s",
        ]
        | None
    ) = Field(default=None)
