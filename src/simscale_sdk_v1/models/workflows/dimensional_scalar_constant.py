from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.dimensional_scalar_object import DimensionalScalarObject


class DimensionalScalarConstant(SimScaleModel):
    value: DimensionalScalarObject | None = Field(default=None)
    value_model_type: str
