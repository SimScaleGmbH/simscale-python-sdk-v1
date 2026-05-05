from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__pressure import Dimensional_Pressure
from simscale_sdk_v1.models.simulation.subdomain_dimensional_initial_condition__pressure import (
    SubdomainDimensionalInitialCondition_Pressure,
)


class DimensionalInitialConditionDomains_Pressure(SimScaleModel):
    global_: Dimensional_Pressure | None = Field(validation_alias="global", serialization_alias="global", default=None)
    subdomains: list[SubdomainDimensionalInitialCondition_Pressure] | None = Field(default=None)
