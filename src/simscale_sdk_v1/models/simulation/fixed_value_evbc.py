from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dynamic_viscosity import Dimensional_DynamicViscosity


class FixedValueEVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE",
        description="Schema name: FixedValueEVBC",
    )
    value: Dimensional_DynamicViscosity | None = Field(default=None)
