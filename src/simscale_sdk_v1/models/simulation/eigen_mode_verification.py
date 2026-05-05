from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EigenModeVerification(SimScaleModel):
    threshold: float | None = Field(default=1e-06)
    precision_shift: float | None = Field(
        validation_alias="precisionShift", serialization_alias="precisionShift", default=0.05
    )
