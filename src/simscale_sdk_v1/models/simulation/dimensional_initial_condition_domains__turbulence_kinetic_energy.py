from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__turbulence_kinetic_energy import Dimensional_TurbulenceKineticEnergy
from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__turbulence_kinetic_energy import (
    SubdomainDimensionalInitialCondition_TurbulenceKineticEnergy,
)


class DimensionalInitialConditionDomains_TurbulenceKineticEnergy(SimScaleModel):
    global_: Dimensional_TurbulenceKineticEnergy | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalInitialCondition_TurbulenceKineticEnergy] | None = Field(default=None)
