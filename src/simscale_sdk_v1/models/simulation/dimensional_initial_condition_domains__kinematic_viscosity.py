from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__kinematic_viscosity import (
    SubdomainDimensionalInitialCondition_KinematicViscosity,
)


class DimensionalInitialConditionDomains_KinematicViscosity(SimScaleModel):
    global_: Dimensional_KinematicViscosity | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalInitialCondition_KinematicViscosity] | None = Field(default=None)
