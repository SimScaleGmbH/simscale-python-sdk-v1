from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__heat_flux import Dimensional_HeatFlux


class FairWeatherConditions(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FAIR_WEATHER_CONDITIONS",
        description="Schema name: FairWeatherConditions",
    )
    sky_cloud_cover_fraction: float | None = Field(
        validation_alias="skyCloudCoverFraction", serialization_alias="skyCloudCoverFraction", default=0
    )
    ground_reflectivity: float | None = Field(
        validation_alias="groundReflectivity", serialization_alias="groundReflectivity", default=0.2
    )
    apparent_solar_irradiation: Dimensional_HeatFlux | None = Field(
        validation_alias="apparentSolarIrradiation", serialization_alias="apparentSolarIrradiation", default=None
    )
    atmospheric_extinction_coefficient: float | None = Field(
        validation_alias="atmosphericExtinctionCoefficient",
        serialization_alias="atmosphericExtinctionCoefficient",
        default=0.142,
        description="Atmospheric extinction coefficient (B)",
    )
    diffuse_radiation_factor: float | None = Field(
        validation_alias="diffuseRadiationFactor",
        serialization_alias="diffuseRadiationFactor",
        default=0.058,
        description="Diffuse radiation factor (C)",
    )
