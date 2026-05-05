from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__heat_flux import Dimensional_HeatFlux


class FluxHeatSource(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="FLUX", description="Schema name: FluxHeatSource"
    )
    heat_flux: Dimensional_HeatFlux | None = Field(
        validation_alias="heatFlux", serialization_alias="heatFlux", default=None
    )
