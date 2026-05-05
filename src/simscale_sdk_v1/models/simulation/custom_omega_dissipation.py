from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__specific_turbulence_dissipation_rate import (
    DimensionalFunction_SpecificTurbulenceDissipationRate,
)


class CustomOmegaDissipation(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_DISSIPATION",
        description="Schema name: CustomOmegaDissipation",
    )
    value: DimensionalFunction_SpecificTurbulenceDissipationRate | None = Field(default=None)
