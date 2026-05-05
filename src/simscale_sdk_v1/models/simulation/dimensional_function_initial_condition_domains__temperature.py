from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__temperature import DimensionalFunction_Temperature
from simscale_sdk_v1.models.simulation.subdomain_dimensional_function_initial_condition__temperature import (
    SubdomainDimensionalFunctionInitialCondition_Temperature,
)


class DimensionalFunctionInitialConditionDomains_Temperature(SimScaleModel):
    global_: DimensionalFunction_Temperature | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalFunctionInitialCondition_Temperature] | None = Field(default=None)
