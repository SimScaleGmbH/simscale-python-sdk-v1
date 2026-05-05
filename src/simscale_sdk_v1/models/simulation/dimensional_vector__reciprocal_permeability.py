from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.decimal_vector import DecimalVector


class DimensionalVector_ReciprocalPermeability(SimScaleModel):
    value: DecimalVector | None = Field(default=None)
    unit: Literal["1/m²", "1/in²", "1/mm²", "1/cm²", "1/ft²", "1/yd²"]
