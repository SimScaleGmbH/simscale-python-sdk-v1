from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__specific_turbulence_dissipation_rate_gradient import (
    Dimensional_SpecificTurbulenceDissipationRateGradient,
)


class FixedGradientOBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientOBC",
    )
    gradient: Dimensional_SpecificTurbulenceDissipationRateGradient | None = Field(default=None)
