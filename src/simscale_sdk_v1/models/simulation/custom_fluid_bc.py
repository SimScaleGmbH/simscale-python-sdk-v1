from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_eddy_viscosity import OneOf_CustomFluidBCEddyViscosity
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_eddy_viscosity_compressible import (
    OneOf_CustomFluidBCEddyViscosityCompressible,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_epsilon_dissipation_rate import (
    OneOf_CustomFluidBCEpsilonDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_gauge_pressure import OneOf_CustomFluidBCGaugePressure
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_gauge_pressure_rgh import (
    OneOf_CustomFluidBCGaugePressureRgh,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_net_radiative_heat_flux import (
    OneOf_CustomFluidBCNetRadiativeHeatFlux,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_nu_tilda import OneOf_CustomFluidBCNuTilda
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_omega_dissipation_rate import (
    OneOf_CustomFluidBCOmegaDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_passive_scalars import OneOf_CustomFluidBCPassiveScalars
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_phase_fraction import OneOf_CustomFluidBCPhaseFraction
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_pressure import OneOf_CustomFluidBCPressure
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_pressure_rgh import OneOf_CustomFluidBCPressureRgh
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_temperature import OneOf_CustomFluidBCTemperature
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_dynamic_viscosity import (
    OneOf_CustomFluidBCTurbulentDynamicViscosity,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_kinetic_energy import (
    OneOf_CustomFluidBCTurbulentKineticEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_thermal_diffusivity import (
    OneOf_CustomFluidBCTurbulentThermalDiffusivity,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_turbulent_thermal_diffusivity_compressible import (
    OneOf_CustomFluidBCTurbulentThermalDiffusivityCompressible,
)
from simscale_sdk_v1.models.simulation.one_of__custom_fluid_bc_velocity import OneOf_CustomFluidBCVelocity
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class CustomFluidBC(SimScaleModel):
    """This boundary condition allows the user to choose conditions for each physical variable separately. It provides full flexibility over the choice of boundary conditions to make advanced customization possible."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CUSTOM_V37",
        description="This boundary condition allows the user to choose conditions for each physical variable separately. It provides full flexibility over the choice of boundary conditions to make advanced customization possible.  Schema name: CustomFluidBC",
    )
    name: str | None = Field(default=None)
    velocity: OneOf_CustomFluidBCVelocity | None = Field(default=None)
    pressure: OneOf_CustomFluidBCPressure | None = Field(default=None)
    pressure_rgh: OneOf_CustomFluidBCPressureRgh | None = Field(
        validation_alias="pressureRgh", serialization_alias="pressureRgh", default=None
    )
    gauge_pressure: OneOf_CustomFluidBCGaugePressure | None = Field(
        validation_alias="gaugePressure", serialization_alias="gaugePressure", default=None
    )
    gauge_pressure_rgh: OneOf_CustomFluidBCGaugePressureRgh | None = Field(
        validation_alias="gaugePressureRgh", serialization_alias="gaugePressureRgh", default=None
    )
    temperature: OneOf_CustomFluidBCTemperature | None = Field(default=None)
    turbulent_kinetic_energy: OneOf_CustomFluidBCTurbulentKineticEnergy | None = Field(
        validation_alias="turbulentKineticEnergy", serialization_alias="turbulentKineticEnergy", default=None
    )
    omega_dissipation_rate: OneOf_CustomFluidBCOmegaDissipationRate | None = Field(
        validation_alias="omegaDissipationRate", serialization_alias="omegaDissipationRate", default=None
    )
    epsilon_dissipation_rate: OneOf_CustomFluidBCEpsilonDissipationRate | None = Field(
        validation_alias="epsilonDissipationRate", serialization_alias="epsilonDissipationRate", default=None
    )
    eddy_viscosity: OneOf_CustomFluidBCEddyViscosity | None = Field(
        validation_alias="eddyViscosity", serialization_alias="eddyViscosity", default=None
    )
    eddy_viscosity_compressible: OneOf_CustomFluidBCEddyViscosityCompressible | None = Field(
        validation_alias="eddyViscosityCompressible", serialization_alias="eddyViscosityCompressible", default=None
    )
    nu_tilda: OneOf_CustomFluidBCNuTilda | None = Field(
        validation_alias="nuTilda", serialization_alias="nuTilda", default=None
    )
    turbulent_thermal_diffusivity: OneOf_CustomFluidBCTurbulentThermalDiffusivity | None = Field(
        validation_alias="turbulentThermalDiffusivity", serialization_alias="turbulentThermalDiffusivity", default=None
    )
    turbulent_thermal_diffusivity_compressible: OneOf_CustomFluidBCTurbulentThermalDiffusivityCompressible | None = (
        Field(
            validation_alias="turbulentThermalDiffusivityCompressible",
            serialization_alias="turbulentThermalDiffusivityCompressible",
            default=None,
        )
    )
    turbulent_dynamic_viscosity: OneOf_CustomFluidBCTurbulentDynamicViscosity | None = Field(
        validation_alias="turbulentDynamicViscosity", serialization_alias="turbulentDynamicViscosity", default=None
    )
    passive_scalars: list[OneOf_CustomFluidBCPassiveScalars] | None = Field(
        validation_alias="passiveScalars",
        serialization_alias="passiveScalars",
        default=None,
        description="Please choose a boundary condition for passive scalar (T).",
    )
    phase_fraction: OneOf_CustomFluidBCPhaseFraction | None = Field(
        validation_alias="phaseFraction", serialization_alias="phaseFraction", default=None
    )
    net_radiative_heat_flux: OneOf_CustomFluidBCNetRadiativeHeatFlux | None = Field(
        validation_alias="netRadiativeHeatFlux", serialization_alias="netRadiativeHeatFlux", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
