from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__turbulent_dissipation import Dimensional_TurbulentDissipation
from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__turbulent_dissipation import (
    SubdomainDimensionalInitialCondition_TurbulentDissipation,
)


class DimensionalInitialConditionDomains_TurbulentDissipation(SimScaleModel):
    global_: Dimensional_TurbulentDissipation | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalInitialCondition_TurbulentDissipation] | None = Field(default=None)
