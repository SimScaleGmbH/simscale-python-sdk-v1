from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.stress_tensor__pressure import StressTensor_Pressure
from simscale_sdk_v1.models.simulation.subdomain_stress_initial_condition import SubdomainStressInitialCondition


class StressInitialConditionDomains(SimScaleModel):
    global_: StressTensor_Pressure | None = Field(validation_alias="global", serialization_alias="global", default=None)
    subdomains: list[SubdomainStressInitialCondition] | None = Field(default=None)
