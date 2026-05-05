from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__dimensionless import (
    DimensionalInitialConditionDomains_Dimensionless,
)
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__kinematic_viscosity import (
    DimensionalInitialConditionDomains_KinematicViscosity,
)
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__pressure import (
    DimensionalInitialConditionDomains_Pressure,
)
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__specific_turbulence_dissipation_rate import (
    DimensionalInitialConditionDomains_SpecificTurbulenceDissipationRate,
)
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__temperature import (
    DimensionalInitialConditionDomains_Temperature,
)
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__turbulence_kinetic_energy import (
    DimensionalInitialConditionDomains_TurbulenceKineticEnergy,
)
from simscale_sdk_v1.models.simulation.dimensional_initial_condition_domains__turbulent_dissipation import (
    DimensionalInitialConditionDomains_TurbulentDissipation,
)
from simscale_sdk_v1.models.simulation.dimensional_vector_initial_condition_domains__speed import (
    DimensionalVectorInitialConditionDomains_Speed,
)
from simscale_sdk_v1.models.simulation.dimensionless_initial_condition_domains import (
    DimensionlessInitialConditionDomains,
)
from simscale_sdk_v1.models.simulation.fraction_values_initial_conditions import FractionValuesInitialConditions


class FluidInitialConditions(SimScaleModel):
    pressure: DimensionalInitialConditionDomains_Pressure | None = Field(default=None)
    pressure_rgh: DimensionalInitialConditionDomains_Pressure | None = Field(
        validation_alias="pressureRgh", serialization_alias="pressureRgh", default=None
    )
    gauge_pressure: DimensionalInitialConditionDomains_Pressure | None = Field(
        validation_alias="gaugePressure", serialization_alias="gaugePressure", default=None
    )
    gauge_pressure_rgh: DimensionalInitialConditionDomains_Pressure | None = Field(
        validation_alias="gaugePressureRgh", serialization_alias="gaugePressureRgh", default=None
    )
    velocity: DimensionalVectorInitialConditionDomains_Speed | None = Field(default=None)
    temperature: DimensionalInitialConditionDomains_Temperature | None = Field(default=None)
    turbulent_kinetic_energy: DimensionalInitialConditionDomains_TurbulenceKineticEnergy | None = Field(
        validation_alias="turbulentKineticEnergy", serialization_alias="turbulentKineticEnergy", default=None
    )
    omega_dissipation_rate: DimensionalInitialConditionDomains_SpecificTurbulenceDissipationRate | None = Field(
        validation_alias="omegaDissipationRate", serialization_alias="omegaDissipationRate", default=None
    )
    epsilon_dissipation_rate: DimensionalInitialConditionDomains_TurbulentDissipation | None = Field(
        validation_alias="epsilonDissipationRate", serialization_alias="epsilonDissipationRate", default=None
    )
    nu_tilda: DimensionalInitialConditionDomains_KinematicViscosity | None = Field(
        validation_alias="nuTilda", serialization_alias="nuTilda", default=None
    )
    passive_scalars: list[DimensionalInitialConditionDomains_Dimensionless] | None = Field(
        validation_alias="passiveScalars", serialization_alias="passiveScalars", default=None
    )
    phase_fraction: DimensionalInitialConditionDomains_Dimensionless | None = Field(
        validation_alias="phaseFraction", serialization_alias="phaseFraction", default=None
    )
    phase_fractions: DimensionlessInitialConditionDomains | None = Field(
        validation_alias="phaseFractions", serialization_alias="phaseFractions", default=None
    )
    mass_fractions: FractionValuesInitialConditions | None = Field(
        validation_alias="massFractions", serialization_alias="massFractions", default=None
    )
    relative_humidity: DimensionalInitialConditionDomains_Dimensionless | None = Field(
        validation_alias="relativeHumidity", serialization_alias="relativeHumidity", default=None
    )
