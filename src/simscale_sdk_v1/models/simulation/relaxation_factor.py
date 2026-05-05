from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RelaxationFactor(SimScaleModel):
    pressure_field: float | None = Field(
        validation_alias="pressureField",
        serialization_alias="pressureField",
        default=None,
        description="With this parameter you can initialize the under-relaxation of a field or equation. The solver will dynamically adapt this factor to improve stability.",
    )
    pressure_rgh_field: float | None = Field(
        validation_alias="pressureRghField", serialization_alias="pressureRghField", default=None
    )
    passive_scalar_equation: float | None = Field(
        validation_alias="passiveScalarEquation", serialization_alias="passiveScalarEquation", default=None
    )
    velocity_equation: float | None = Field(
        validation_alias="velocityEquation",
        serialization_alias="velocityEquation",
        default=None,
        description="With this parameter you can initialize the under-relaxation of a field or equation. The solver will dynamically adapt this factor to improve stability.",
    )
    velocity: float | None = Field(default=None)
    temperature_equation: float | None = Field(
        validation_alias="temperatureEquation", serialization_alias="temperatureEquation", default=None
    )
    temperature_field: float | None = Field(
        validation_alias="temperatureField", serialization_alias="temperatureField", default=None
    )
    density_field: float | None = Field(
        validation_alias="densityField", serialization_alias="densityField", default=None
    )
    enthalpy_equation: float | None = Field(
        validation_alias="enthalpyEquation",
        serialization_alias="enthalpyEquation",
        default=None,
        description="With this parameter you can initialize the under-relaxation of a field or equation. The solver will dynamically adapt this factor to improve stability.",
    )
    internal_energy_equation: float | None = Field(
        validation_alias="internalEnergyEquation",
        serialization_alias="internalEnergyEquation",
        default=None,
        description="With this parameter you can initialize the under-relaxation of a field or equation. The solver will dynamically adapt this factor to improve stability.",
    )
    turbulent_kinetic_energy_equation: float | None = Field(
        validation_alias="turbulentKineticEnergyEquation",
        serialization_alias="turbulentKineticEnergyEquation",
        default=None,
    )
    omega_dissipation_rate_equation: float | None = Field(
        validation_alias="omegaDissipationRateEquation",
        serialization_alias="omegaDissipationRateEquation",
        default=None,
    )
    epsilon_dissipation_rate_equation: float | None = Field(
        validation_alias="epsilonDissipationRateEquation",
        serialization_alias="epsilonDissipationRateEquation",
        default=None,
    )
    turbulent_kinetic_energy: float | None = Field(
        validation_alias="turbulentKineticEnergy", serialization_alias="turbulentKineticEnergy", default=None
    )
    turbulent_energy_dissipation_rate: float | None = Field(
        validation_alias="turbulentEnergyDissipationRate",
        serialization_alias="turbulentEnergyDissipationRate",
        default=None,
    )
    nu_tilda_equation: float | None = Field(
        validation_alias="nuTildaEquation", serialization_alias="nuTildaEquation", default=None
    )
    net_radiative_heat_flux_field: float | None = Field(
        validation_alias="netRadiativeHeatFluxField", serialization_alias="netRadiativeHeatFluxField", default=None
    )
    internal_energy: float | None = Field(
        validation_alias="internalEnergy", serialization_alias="internalEnergy", default=None
    )
    gas_mixture_transport: float | None = Field(
        validation_alias="gasMixtureTransport", serialization_alias="gasMixtureTransport", default=0.0
    )
    radiative_intensity_ray_equation: float | None = Field(
        validation_alias="radiativeIntensityRayEquation",
        serialization_alias="radiativeIntensityRayEquation",
        default=0.8,
    )
    radiative_intensity_ray_field: float | None = Field(
        validation_alias="radiativeIntensityRayField", serialization_alias="radiativeIntensityRayField", default=0.8
    )
    specific_humidity_equation: float | None = Field(
        validation_alias="specificHumidityEquation", serialization_alias="specificHumidityEquation", default=0.7
    )
    age_of_fluid_equation: float | None = Field(
        validation_alias="ageOfFluidEquation", serialization_alias="ageOfFluidEquation", default=None
    )
    voltage_field: float | None = Field(
        validation_alias="voltageField", serialization_alias="voltageField", default=0.5
    )
