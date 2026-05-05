from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_function__angle_value import (
    OneOf_DimensionalFunction_AngleValue,
)


class DimensionalFunction_Angle(SimScaleModel):
    value: OneOf_DimensionalFunction_AngleValue | None = Field(default=None)
    unit: Literal["rad", "°"]
