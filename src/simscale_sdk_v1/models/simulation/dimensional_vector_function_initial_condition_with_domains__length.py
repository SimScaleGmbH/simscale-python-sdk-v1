from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector_function__length import DimensionalVectorFunction_Length
from simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__length import (
    SubdomainBasedDimensionalVectorFunctionInitialCondition_Length,
)


class DimensionalVectorFunctionInitialConditionWithDomains_Length(SimScaleModel):
    global_: DimensionalVectorFunction_Length | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainBasedDimensionalVectorFunctionInitialCondition_Length] | None = Field(default=None)
