from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_vector_function__force_value import (
    OneOf_DimensionalVectorFunction_ForceValue,
)


class DimensionalVectorFunction_Force(SimScaleModel):
    value: OneOf_DimensionalVectorFunction_ForceValue | None = Field(default=None)
    unit: Literal["N", "lbf", "dyne", "µN"]
