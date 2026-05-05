from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__epsilon_gradient import Dimensional_EpsilonGradient


class FixedGradientEBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientEBC",
    )
    gradient: Dimensional_EpsilonGradient | None = Field(default=None)
