from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__specific_turbulence_dissipation_rate import (
    DimensionalFunction_SpecificTurbulenceDissipationRate,
)
from simscale_sdk_v1.models.simulation.dimensional_function__turbulence_kinetic_energy import (
    DimensionalFunction_TurbulenceKineticEnergy,
)
from simscale_sdk_v1.models.simulation.dimensional_function__turbulent_dissipation import (
    DimensionalFunction_TurbulentDissipation,
)


class FixedValueTurbulence(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE_TURBULENCE",
        description="Schema name: FixedValueTurbulence",
    )
    turbulent_kinetic_energy: DimensionalFunction_TurbulenceKineticEnergy | None = Field(
        validation_alias="turbulentKineticEnergy", serialization_alias="turbulentKineticEnergy", default=None
    )
    epsilon_dissipation_rate: DimensionalFunction_TurbulentDissipation | None = Field(
        validation_alias="epsilonDissipationRate", serialization_alias="epsilonDissipationRate", default=None
    )
    omega_dissipation_rate: DimensionalFunction_SpecificTurbulenceDissipationRate | None = Field(
        validation_alias="omegaDissipationRate", serialization_alias="omegaDissipationRate", default=None
    )
