from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure


class FixedValuePBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE",
        description="Schema name: FixedValuePBC",
    )
    value: DimensionalFunction_Pressure | None = Field(default=None)
