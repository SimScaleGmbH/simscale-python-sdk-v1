from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature_gradient import (
    DimensionalFunction_TemperatureGradient,
)


class FixedGradientTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientTBC",
    )
    gradient: DimensionalFunction_TemperatureGradient | None = Field(default=None)
