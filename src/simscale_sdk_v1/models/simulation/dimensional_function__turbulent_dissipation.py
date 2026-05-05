from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__turbulent_dissipation_value import (
    OneOf_DimensionalFunction_TurbulentDissipationValue,
)


class DimensionalFunction_TurbulentDissipation(SimScaleModel):
    value: OneOf_DimensionalFunction_TurbulentDissipationValue | None = Field(default=None)
    unit: Literal["m²/s³", "lbf·in/(s·lb)"]
