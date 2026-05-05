from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__eddy_viscosity_gradient import Dimensional_EddyViscosityGradient


class SurfaceWaterVaporFluxHumidityBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SURFACE_WATER_VAPOR_FLUX",
        description="Schema name: SurfaceWaterVaporFluxHumidityBC",
    )
    water_vapor_flux: Dimensional_EddyViscosityGradient | None = Field(
        validation_alias="waterVaporFlux", serialization_alias="waterVaporFlux", default=None
    )
