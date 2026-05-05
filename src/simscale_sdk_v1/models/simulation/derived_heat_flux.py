from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__heat_flux import Dimensional_HeatFlux
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature
from simscale_sdk_v1.models.simulation.dimensional__thermal_transmittance import Dimensional_ThermalTransmittance
from simscale_sdk_v1.models.simulation.one_of__derived_heat_flux_wall_thermal import OneOf_DerivedHeatFluxWallThermal


class DerivedHeatFlux(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DERIVED",
        description="Schema name: DerivedHeatFlux",
    )
    heat_transfer_coefficient: Dimensional_ThermalTransmittance | None = Field(
        validation_alias="heatTransferCoefficient", serialization_alias="heatTransferCoefficient", default=None
    )
    ambient_temperature: Dimensional_Temperature | None = Field(
        validation_alias="ambientTemperature", serialization_alias="ambientTemperature", default=None
    )
    additional_heat_flux: Dimensional_HeatFlux | None = Field(
        validation_alias="additionalHeatFlux", serialization_alias="additionalHeatFlux", default=None
    )
    wall_thermal: OneOf_DerivedHeatFluxWallThermal | None = Field(
        validation_alias="wallThermal", serialization_alias="wallThermal", default=None
    )
    outer_surface_emissivity: float | None = Field(
        validation_alias="outerSurfaceEmissivity",
        serialization_alias="outerSurfaceEmissivity",
        default=0.9,
        description="Emissivity/Absorptivity of the outer side of the surface or the last wall thermal layer.",
    )
