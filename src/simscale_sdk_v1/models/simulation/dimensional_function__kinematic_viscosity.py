from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__kinematic_viscosity_value import (
    OneOf_DimensionalFunction_KinematicViscosityValue,
)


class DimensionalFunction_KinematicViscosity(SimScaleModel):
    value: OneOf_DimensionalFunction_KinematicViscosityValue | None = Field(default=None)
    unit: Literal["m²/s", "lbf·s·in/lb", "ft²/s", "in²/s"]
