from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__electric_potential import (
    DimensionalFunction_ElectricPotential,
)


class FixedElectricPotentialEBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_ELECTRIC_POTENTIAL",
        description="Schema name: FixedElectricPotentialEBC",
    )
    potential_function: DimensionalFunction_ElectricPotential | None = Field(
        validation_alias="potentialFunction", serialization_alias="potentialFunction", default=None
    )
