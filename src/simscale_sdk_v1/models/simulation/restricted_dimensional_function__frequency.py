from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__restricted_dimensional_function__frequency_value import (
    OneOf_RestrictedDimensionalFunction_FrequencyValue,
)


class RestrictedDimensionalFunction_Frequency(SimScaleModel):
    value: OneOf_RestrictedDimensionalFunction_FrequencyValue | None = Field(default=None)
    unit: Literal["1/s", "RPM", "Hz"]
