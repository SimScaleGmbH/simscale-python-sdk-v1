from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.one_of__external_wall_heat_flux_tbc_heat_flux import (
    OneOf_ExternalWallHeatFluxTBCHeatFlux,
)


class ExternalWallHeatFluxTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="EXTERNAL_WALL_HEAT_FLUX_TEMPERATURE",
        description="Schema name: ExternalWallHeatFluxTBC",
    )
    heat_flux: OneOf_ExternalWallHeatFluxTBCHeatFlux | None = Field(
        validation_alias="heatFlux", serialization_alias="heatFlux", default=None
    )
    value: Dimensional_Temperature | None = Field(default=None)
