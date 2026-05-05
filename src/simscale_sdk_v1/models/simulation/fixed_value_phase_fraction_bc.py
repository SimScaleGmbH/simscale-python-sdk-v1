from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FixedValuePhaseFractionBC(SimScaleModel):
    associated_phase: Literal["PHASE_0", "PHASE_1"] | None = Field(
        validation_alias="associatedPhase", serialization_alias="associatedPhase", default="PHASE_0"
    )
    fraction_value: float | None = Field(
        validation_alias="fractionValue", serialization_alias="fractionValue", default=0.0
    )
