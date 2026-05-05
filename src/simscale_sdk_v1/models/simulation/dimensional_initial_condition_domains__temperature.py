from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__temperature import (
    SubdomainDimensionalInitialCondition_Temperature,
)


class DimensionalInitialConditionDomains_Temperature(SimScaleModel):
    global_: Dimensional_Temperature | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalInitialCondition_Temperature] | None = Field(default=None)
