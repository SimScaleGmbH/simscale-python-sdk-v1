from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__specific_turbulence_dissipation_rate import (
    DimensionalVector_SpecificTurbulenceDissipationRate,
)


class FixedGradientVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientVBC",
    )
    gradient: DimensionalVector_SpecificTurbulenceDissipationRate | None = Field(default=None)
