from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__mass_flow_rate_value import (
    OneOf_DimensionalFunction_MassFlowRateValue,
)


class DimensionalFunction_MassFlowRate(SimScaleModel):
    value: OneOf_DimensionalFunction_MassFlowRateValue | None = Field(default=None)
    unit: Literal[
        "kg/s", "lb/s", "kg/min", "kg/h", "g/s", "g/min", "g/h", "lb/min", "lb/h", "slug/s", "slug/min", "slug/h"
    ]
