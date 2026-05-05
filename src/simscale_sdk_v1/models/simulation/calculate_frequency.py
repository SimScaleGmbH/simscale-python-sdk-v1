from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CalculateFrequency(SimScaleModel):
    prec_shift: float | None = Field(validation_alias="precShift", serialization_alias="precShift", default=0.05)
    max_iter_shift: int | None = Field(validation_alias="maxIterShift", serialization_alias="maxIterShift", default=3)
    threshold_frequency: float | None = Field(
        validation_alias="thresholdFrequency", serialization_alias="thresholdFrequency", default=0.01
    )
