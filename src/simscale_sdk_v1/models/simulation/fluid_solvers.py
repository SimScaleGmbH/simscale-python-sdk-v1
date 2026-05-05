from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.mules_solver import MULESSolver
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_density_final_solver import (
    OneOf_FluidSolversDensityFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_density_solver import OneOf_FluidSolversDensitySolver
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_enthalpy_final_solver import (
    OneOf_FluidSolversEnthalpyFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_enthalpy_solver import OneOf_FluidSolversEnthalpySolver
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_epsilon_dissipation_rate_final_solver import (
    OneOf_FluidSolversEpsilonDissipationRateFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_epsilon_dissipation_rate_solver import (
    OneOf_FluidSolversEpsilonDissipationRateSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_internal_energy_final_solver import (
    OneOf_FluidSolversInternalEnergyFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_internal_energy_solver import (
    OneOf_FluidSolversInternalEnergySolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_nu_tilda_final_solver import (
    OneOf_FluidSolversNuTildaFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_nu_tilda_solver import OneOf_FluidSolversNuTildaSolver
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_omega_dissipation_rate_final_solver import (
    OneOf_FluidSolversOmegaDissipationRateFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_omega_dissipation_rate_solver import (
    OneOf_FluidSolversOmegaDissipationRateSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_passive_scalar_solver import (
    OneOf_FluidSolversPassiveScalarSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_final_solver import (
    OneOf_FluidSolversPressureFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_rgh_final_solver import (
    OneOf_FluidSolversPressureRghFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_rgh_solver import (
    OneOf_FluidSolversPressureRghSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_pressure_solver import OneOf_FluidSolversPressureSolver
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_radiative_intensity_ray_solver import (
    OneOf_FluidSolversRadiativeIntensityRaySolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_solid_enthalpy_final_solver import (
    OneOf_FluidSolversSolidEnthalpyFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_solid_enthalpy_solver import (
    OneOf_FluidSolversSolidEnthalpySolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_specific_humidity_solver import (
    OneOf_FluidSolversSpecificHumiditySolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_temperature_final_solver import (
    OneOf_FluidSolversTemperatureFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_temperature_solver import (
    OneOf_FluidSolversTemperatureSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_turbulent_kinetic_energy_final_solver import (
    OneOf_FluidSolversTurbulentKineticEnergyFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_turbulent_kinetic_energy_solver import (
    OneOf_FluidSolversTurbulentKineticEnergySolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_velocity_final_solver import (
    OneOf_FluidSolversVelocityFinalSolver,
)
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_velocity_solver import OneOf_FluidSolversVelocitySolver
from simscale_sdk_v1.models.simulation.one_of__fluid_solvers_voltage_solver import OneOf_FluidSolversVoltageSolver
from simscale_sdk_v1.models.simulation.pbicg_stab_solver import PBICGStabSolver


class FluidSolvers(SimScaleModel):
    phase_fraction_solver: MULESSolver | None = Field(
        validation_alias="phaseFractionSolver", serialization_alias="phaseFractionSolver", default=None
    )
    velocity_solver: OneOf_FluidSolversVelocitySolver | None = Field(
        validation_alias="velocitySolver", serialization_alias="velocitySolver", default=None
    )
    velocity_final_solver: OneOf_FluidSolversVelocityFinalSolver | None = Field(
        validation_alias="velocityFinalSolver", serialization_alias="velocityFinalSolver", default=None
    )
    density_solver: OneOf_FluidSolversDensitySolver | None = Field(
        validation_alias="densitySolver", serialization_alias="densitySolver", default=None
    )
    density_final_solver: OneOf_FluidSolversDensityFinalSolver | None = Field(
        validation_alias="densityFinalSolver", serialization_alias="densityFinalSolver", default=None
    )
    pressure_solver: OneOf_FluidSolversPressureSolver | None = Field(
        validation_alias="pressureSolver", serialization_alias="pressureSolver", default=None
    )
    pressure_final_solver: OneOf_FluidSolversPressureFinalSolver | None = Field(
        validation_alias="pressureFinalSolver", serialization_alias="pressureFinalSolver", default=None
    )
    temperature_solver: OneOf_FluidSolversTemperatureSolver | None = Field(
        validation_alias="temperatureSolver", serialization_alias="temperatureSolver", default=None
    )
    temperature_final_solver: OneOf_FluidSolversTemperatureFinalSolver | None = Field(
        validation_alias="temperatureFinalSolver", serialization_alias="temperatureFinalSolver", default=None
    )
    pressure_rgh_solver: OneOf_FluidSolversPressureRghSolver | None = Field(
        validation_alias="pressureRghSolver", serialization_alias="pressureRghSolver", default=None
    )
    pressure_rgh_final_solver: OneOf_FluidSolversPressureRghFinalSolver | None = Field(
        validation_alias="pressureRghFinalSolver", serialization_alias="pressureRghFinalSolver", default=None
    )
    solid_enthalpy_solver: OneOf_FluidSolversSolidEnthalpySolver | None = Field(
        validation_alias="solidEnthalpySolver", serialization_alias="solidEnthalpySolver", default=None
    )
    solid_enthalpy_final_solver: OneOf_FluidSolversSolidEnthalpyFinalSolver | None = Field(
        validation_alias="solidEnthalpyFinalSolver", serialization_alias="solidEnthalpyFinalSolver", default=None
    )
    enthalpy_solver: OneOf_FluidSolversEnthalpySolver | None = Field(
        validation_alias="enthalpySolver", serialization_alias="enthalpySolver", default=None
    )
    enthalpy_final_solver: OneOf_FluidSolversEnthalpyFinalSolver | None = Field(
        validation_alias="enthalpyFinalSolver", serialization_alias="enthalpyFinalSolver", default=None
    )
    internal_energy_solver: OneOf_FluidSolversInternalEnergySolver | None = Field(
        validation_alias="internalEnergySolver", serialization_alias="internalEnergySolver", default=None
    )
    internal_energy_final_solver: OneOf_FluidSolversInternalEnergyFinalSolver | None = Field(
        validation_alias="internalEnergyFinalSolver", serialization_alias="internalEnergyFinalSolver", default=None
    )
    turbulent_kinetic_energy_solver: OneOf_FluidSolversTurbulentKineticEnergySolver | None = Field(
        validation_alias="turbulentKineticEnergySolver",
        serialization_alias="turbulentKineticEnergySolver",
        default=None,
    )
    turbulent_kinetic_energy_final_solver: OneOf_FluidSolversTurbulentKineticEnergyFinalSolver | None = Field(
        validation_alias="turbulentKineticEnergyFinalSolver",
        serialization_alias="turbulentKineticEnergyFinalSolver",
        default=None,
    )
    nu_tilda_solver: OneOf_FluidSolversNuTildaSolver | None = Field(
        validation_alias="nuTildaSolver", serialization_alias="nuTildaSolver", default=None
    )
    nu_tilda_final_solver: OneOf_FluidSolversNuTildaFinalSolver | None = Field(
        validation_alias="nuTildaFinalSolver", serialization_alias="nuTildaFinalSolver", default=None
    )
    omega_dissipation_rate_solver: OneOf_FluidSolversOmegaDissipationRateSolver | None = Field(
        validation_alias="omegaDissipationRateSolver", serialization_alias="omegaDissipationRateSolver", default=None
    )
    omega_dissipation_rate_final_solver: OneOf_FluidSolversOmegaDissipationRateFinalSolver | None = Field(
        validation_alias="omegaDissipationRateFinalSolver",
        serialization_alias="omegaDissipationRateFinalSolver",
        default=None,
    )
    epsilon_dissipation_rate_solver: OneOf_FluidSolversEpsilonDissipationRateSolver | None = Field(
        validation_alias="epsilonDissipationRateSolver",
        serialization_alias="epsilonDissipationRateSolver",
        default=None,
    )
    epsilon_dissipation_rate_final_solver: OneOf_FluidSolversEpsilonDissipationRateFinalSolver | None = Field(
        validation_alias="epsilonDissipationRateFinalSolver",
        serialization_alias="epsilonDissipationRateFinalSolver",
        default=None,
    )
    passive_scalar_solver: OneOf_FluidSolversPassiveScalarSolver | None = Field(
        validation_alias="passiveScalarSolver", serialization_alias="passiveScalarSolver", default=None
    )
    radiative_intensity_ray_solver: OneOf_FluidSolversRadiativeIntensityRaySolver | None = Field(
        validation_alias="radiativeIntensityRaySolver", serialization_alias="radiativeIntensityRaySolver", default=None
    )
    internal_net_radiative_heat_flux_solver: PBICGStabSolver | None = Field(
        validation_alias="internalNetRadiativeHeatFluxSolver",
        serialization_alias="internalNetRadiativeHeatFluxSolver",
        default=None,
    )
    specific_humidity_solver: OneOf_FluidSolversSpecificHumiditySolver | None = Field(
        validation_alias="specificHumiditySolver", serialization_alias="specificHumiditySolver", default=None
    )
    voltage_solver: OneOf_FluidSolversVoltageSolver | None = Field(
        validation_alias="voltageSolver", serialization_alias="voltageSolver", default=None
    )
