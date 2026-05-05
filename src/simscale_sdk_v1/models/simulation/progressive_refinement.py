from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ProgressiveRefinement(SimScaleModel):
    enable_progressive_refinement: bool | None = Field(
        validation_alias="enableProgressiveRefinement", serialization_alias="enableProgressiveRefinement", default=True
    )
    base_refinement_fraction: float | None = Field(
        validation_alias="baseRefinementFraction", serialization_alias="baseRefinementFraction", default=0.4
    )
    full_refinement_fraction: float | None = Field(
        validation_alias="fullRefinementFraction", serialization_alias="fullRefinementFraction", default=0.3
    )
