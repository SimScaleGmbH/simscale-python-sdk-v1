from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__temperature import (
    DimensionalInitialConditionDomains_Temperature,
)


class ElectromagneticInitialConditions(SimScaleModel):
    temperature: DimensionalInitialConditionDomains_Temperature | None = Field(default=None)
