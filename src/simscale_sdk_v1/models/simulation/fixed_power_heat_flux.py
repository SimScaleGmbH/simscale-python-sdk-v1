from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__power import DimensionalFunction_Power


class FixedPowerHeatFlux(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_POWER",
        description="Schema name: FixedPowerHeatFlux",
    )
    function: DimensionalFunction_Power | None = Field(default=None)
