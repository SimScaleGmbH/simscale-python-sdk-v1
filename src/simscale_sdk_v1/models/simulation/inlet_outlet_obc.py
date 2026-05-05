from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__specific_turbulence_dissipation_rate import (
    Dimensional_SpecificTurbulenceDissipationRate,
)


class InletOutletOBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_OUTLET",
        description="Schema name: InletOutletOBC",
    )
    value: Dimensional_SpecificTurbulenceDissipationRate | None = Field(default=None)
