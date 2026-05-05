from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.partial_vector_function import PartialVectorFunction


class DimensionalPartialVectorFunction_Angle(SimScaleModel):
    value: PartialVectorFunction | None = Field(default=None)
    unit: Literal["rad", "°"]
