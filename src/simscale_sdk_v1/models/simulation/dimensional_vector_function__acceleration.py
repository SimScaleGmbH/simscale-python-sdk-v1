from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__acceleration_value import (
    OneOf_DimensionalVectorFunction_AccelerationValue,
)


class DimensionalVectorFunction_Acceleration(SimScaleModel):
    value: OneOf_DimensionalVectorFunction_AccelerationValue | None = Field(default=None)
    unit: Literal["m/s²", "in/s²", "G"]
