from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.measured_value import MeasuredValue


class MeasureEntitiesResponse(SimScaleModel):
    message: str | None = Field(default=None, description="Message describing the measure.")
    measured: list[MeasuredValue] | None = Field(default=None, description="Measure results.")
