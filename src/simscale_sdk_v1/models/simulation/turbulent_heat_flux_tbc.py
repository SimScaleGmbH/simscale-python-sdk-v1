from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.one_of__turbulent_heat_flux_tbc_heat_source import (
    OneOf_TurbulentHeatFluxTBCHeatSource,
)


class TurbulentHeatFluxTBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TURBULENT_HEAT_FLUX_TEMPERATURE",
        description="Schema name: TurbulentHeatFluxTBC",
    )
    heat_source: OneOf_TurbulentHeatFluxTBCHeatSource | None = Field(
        validation_alias="heatSource", serialization_alias="heatSource", default=None
    )
    value: Dimensional_Temperature | None = Field(default=None)
