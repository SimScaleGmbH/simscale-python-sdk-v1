from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.tolerance import Tolerance


class ResidualControls(SimScaleModel):
    velocity: Tolerance | None = Field(default=None)
    pressure: Tolerance | None = Field(default=None)
    pressure_rgh: Tolerance | None = Field(
        validation_alias="pressureRgh", serialization_alias="pressureRgh", default=None
    )
    temperature: Tolerance | None = Field(default=None)
    turbulent_kinetic_energy: Tolerance | None = Field(
        validation_alias="turbulentKineticEnergy", serialization_alias="turbulentKineticEnergy", default=None
    )
    omega_dissipation_rate: Tolerance | None = Field(
        validation_alias="omegaDissipationRate", serialization_alias="omegaDissipationRate", default=None
    )
    epsilon_dissipation_rate: Tolerance | None = Field(
        validation_alias="epsilonDissipationRate", serialization_alias="epsilonDissipationRate", default=None
    )
