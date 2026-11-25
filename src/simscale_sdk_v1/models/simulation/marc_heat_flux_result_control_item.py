from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.global_heat_flux import GlobalHeatFlux


class MarcHeatFluxResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HEAT_FLUX",
        description="Schema name: MarcHeatFluxResultControlItem",
    )
    name: str | None = Field(default=None)
    heat_flux_type: GlobalHeatFlux | None = Field(
        validation_alias="heatFluxType", serialization_alias="heatFluxType", default=None
    )
