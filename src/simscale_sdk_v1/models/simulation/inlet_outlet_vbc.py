from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_vector__speed import DimensionalVector_Speed


class InletOutletVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_OUTLET",
        description="Schema name: InletOutletVBC",
    )
    value: DimensionalVector_Speed | None = Field(default=None)
