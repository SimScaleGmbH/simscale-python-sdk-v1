from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AdaptiveAugmentation(SimScaleModel):
    field_change_target_value: float | None = Field(
        validation_alias="fieldChangeTargetValue",
        serialization_alias="fieldChangeTargetValue",
        default=0.01,
        description="Define the percentage of additional Newton Iterations that should be allowed to be used if convergence is not reached after the maximum number of Newton Iterations is reached.",
    )
