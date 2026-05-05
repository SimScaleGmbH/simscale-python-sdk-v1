from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function_initial_condition_domains__temperature import (
    DimensionalFunctionInitialConditionDomains_Temperature,
)
from simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__acceleration import (
    DimensionalVectorFunctionInitialConditionWithDomains_Acceleration,
)
from simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__length import (
    DimensionalVectorFunctionInitialConditionWithDomains_Length,
)
from simscale_sdk_v1.models.simulation.dimensional_vector_function_initial_condition_with_domains__speed import (
    DimensionalVectorFunctionInitialConditionWithDomains_Speed,
)
from simscale_sdk_v1.models.simulation.stress_initial_condition_domains import StressInitialConditionDomains


class SolidInitialConditions(SimScaleModel):
    displacement: DimensionalVectorFunctionInitialConditionWithDomains_Length | None = Field(default=None)
    velocity: DimensionalVectorFunctionInitialConditionWithDomains_Speed | None = Field(default=None)
    acceleration: DimensionalVectorFunctionInitialConditionWithDomains_Acceleration | None = Field(default=None)
    stress: StressInitialConditionDomains | None = Field(default=None)
    temperature: DimensionalFunctionInitialConditionDomains_Temperature | None = Field(default=None)
