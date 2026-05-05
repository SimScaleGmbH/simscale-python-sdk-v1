from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__restricted_dimensional_function__time_value import (
    OneOf_RestrictedDimensionalFunction_TimeValue,
)


class RestrictedDimensionalFunction_Time(SimScaleModel):
    value: OneOf_RestrictedDimensionalFunction_TimeValue | None = Field(default=None)
    unit: Literal["s"]
