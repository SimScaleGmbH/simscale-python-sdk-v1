from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fraction_value_initial_condition import FractionValueInitialCondition
from simscale_sdk_v1.models.simulation.subdomain_fraction_value_initial_condition import (
    SubdomainFractionValueInitialCondition,
)


class FractionValuesInitialConditions(SimScaleModel):
    global_: list[FractionValueInitialCondition] | None = Field(
        validation_alias="global", serialization_alias="global", default=None
    )
    subdomains: list[SubdomainFractionValueInitialCondition] | None = Field(default=None)
