from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__specific_turbulence_dissipation_rate import (
    Dimensional_SpecificTurbulenceDissipationRate,
)
from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__specific_turbulence_dissipation_rate import (
    SubdomainDimensionalInitialCondition_SpecificTurbulenceDissipationRate,
)


class DimensionalInitialConditionDomains_SpecificTurbulenceDissipationRate(SimScaleModel):
    global_: Dimensional_SpecificTurbulenceDissipationRate | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalInitialCondition_SpecificTurbulenceDissipationRate] | None = Field(
        default=None
    )
