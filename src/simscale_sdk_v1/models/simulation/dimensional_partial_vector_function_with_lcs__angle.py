from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__dimensional_partial_vector_function_with_lcs__angle_value import (
    OneOf_DimensionalPartialVectorFunctionWithLCS_AngleValue,
)


class DimensionalPartialVectorFunctionWithLCS_Angle(SimScaleModel):
    value: OneOf_DimensionalPartialVectorFunctionWithLCS_AngleValue | None = Field(default=None)
    unit: Literal["rad", "°"]
