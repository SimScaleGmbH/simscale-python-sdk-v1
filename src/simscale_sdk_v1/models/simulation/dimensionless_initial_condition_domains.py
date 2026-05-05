from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.subdomain_dimensionless_initial_condition import (
    SubdomainDimensionlessInitialCondition,
)


class DimensionlessInitialConditionDomains(SimScaleModel):
    subdomains: list[SubdomainDimensionlessInitialCondition] | None = Field(default=None)
