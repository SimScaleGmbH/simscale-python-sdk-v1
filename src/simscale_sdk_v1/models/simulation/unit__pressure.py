from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Unit_Pressure(SimScaleModel):
    value: float | None = Field(default=None)
    unit: (
        Literal[
            "Pa",
            "lbf/in²",
            "hPa",
            "kPa",
            "MPa",
            "atm",
            "mbar",
            "bar",
            "mH2O",
            "mmH2O",
            "mmHg",
            "dyne/cm²",
            "inH2O",
            "ftH2O",
            "inHg",
            "psf",
        ]
        | None
    ) = Field(default=None)
