from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__pressure_value import (
    OneOf_DimensionalFunction_PressureValue,
)


class DimensionalFunction_Pressure(SimScaleModel):
    value: OneOf_DimensionalFunction_PressureValue | None = Field(default=None)
    unit: Literal[
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
