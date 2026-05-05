from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed
from simscale_sdk_v1.models.simulation.subdomain_dimensional_vector_initial_condition__speed import (
    SubdomainDimensionalVectorInitialCondition_Speed,
)


class DimensionalVectorInitialConditionDomains_Speed(SimScaleModel):
    global_: DimensionalVector_Speed | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainDimensionalVectorInitialCondition_Speed] | None = Field(default=None)
