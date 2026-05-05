from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector_function__acceleration import (
    DimensionalVectorFunction_Acceleration,
)
from simscale_sdk_v1.models.simulation.subdomain_based_dimensional_vector_function_initial_condition__acceleration import (
    SubdomainBasedDimensionalVectorFunctionInitialCondition_Acceleration,
)


class DimensionalVectorFunctionInitialConditionWithDomains_Acceleration(SimScaleModel):
    global_: DimensionalVectorFunction_Acceleration | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainBasedDimensionalVectorFunctionInitialCondition_Acceleration] | None = Field(default=None)
