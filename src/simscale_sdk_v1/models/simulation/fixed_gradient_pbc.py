from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__force_density import Dimensional_ForceDensity


class FixedGradientPBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientPBC",
    )
    gradient: Dimensional_ForceDensity | None = Field(default=None)
