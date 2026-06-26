from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MeasurementUnitConstant(SimScaleModel):
    value: str | None = Field(default=None)
    value_model_type: str
