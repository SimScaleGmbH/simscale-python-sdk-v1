from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__phase_fraction_gradient import Dimensional_PhaseFractionGradient


class FixedGradientPFBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientPFBC",
    )
    gradient: Dimensional_PhaseFractionGradient | None = Field(default=None)
