from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__heat_flux import Dimensional_HeatFlux


class CustomSolarLoad(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_SOLAR_LOAD",
        description="Schema name: CustomSolarLoad",
    )
    direct_solar_load: Dimensional_HeatFlux | None = Field(
        validation_alias="directSolarLoad", serialization_alias="directSolarLoad", default=None
    )
    diffuse_solar_load: Dimensional_HeatFlux | None = Field(
        validation_alias="diffuseSolarLoad", serialization_alias="diffuseSolarLoad", default=None
    )
