from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__heat_flux import DimensionalFunction_HeatFlux


class FixedHeatFlux(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="FIXED", description="Schema name: FixedHeatFlux"
    )
    function: DimensionalFunction_HeatFlux | None = Field(default=None)
