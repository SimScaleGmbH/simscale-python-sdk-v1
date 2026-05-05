from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__dimensionless import (
    SubdomainDimensionalInitialCondition_Dimensionless,
)


class DimensionalInitialConditionDomains_Dimensionless(SimScaleModel):
    global_: Dimensional_Dimensionless | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalInitialCondition_Dimensionless] | None = Field(default=None)
