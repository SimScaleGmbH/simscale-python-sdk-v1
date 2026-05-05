from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__absorptivity import Dimensional_Absorptivity


class FixedGradientPSBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientPSBC",
    )
    gradient: Dimensional_Absorptivity | None = Field(default=None)
