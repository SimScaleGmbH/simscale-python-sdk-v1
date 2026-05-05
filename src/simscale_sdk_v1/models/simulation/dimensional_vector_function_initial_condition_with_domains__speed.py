from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector_function__speed import DimensionalVectorFunction_Speed
from simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__speed import (
    SubdomainBasedDimensionalVectorFunctionInitialCondition_Speed,
)


class DimensionalVectorFunctionInitialConditionWithDomains_Speed(SimScaleModel):
    global_: DimensionalVectorFunction_Speed | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainBasedDimensionalVectorFunctionInitialCondition_Speed] | None = Field(default=None)
