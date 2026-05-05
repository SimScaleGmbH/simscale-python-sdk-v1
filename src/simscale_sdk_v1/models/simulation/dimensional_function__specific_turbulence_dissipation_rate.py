from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__specific_turbulence_dissipation_rate_value import (
    OneOf_DimensionalFunction_SpecificTurbulenceDissipationRateValue,
)


class DimensionalFunction_SpecificTurbulenceDissipationRate(SimScaleModel):
    value: OneOf_DimensionalFunction_SpecificTurbulenceDissipationRateValue | None = Field(default=None)
    unit: Literal["1/s"]
