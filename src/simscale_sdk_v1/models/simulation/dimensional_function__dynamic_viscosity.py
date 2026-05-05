from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__dynamic_viscosity_value import (
    OneOf_DimensionalFunction_DynamicViscosityValue,
)


class DimensionalFunction_DynamicViscosity(SimScaleModel):
    value: OneOf_DimensionalFunction_DynamicViscosityValue | None = Field(default=None)
    unit: Literal["kg/(s·m)", "lbf·s/in²"]
