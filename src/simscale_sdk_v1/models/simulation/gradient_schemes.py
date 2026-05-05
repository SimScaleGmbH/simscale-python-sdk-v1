from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_for_default import OneOf_GradientSchemesForDefault
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_density import OneOf_GradientSchemesGrad_density
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_enthalpy import OneOf_GradientSchemesGrad_enthalpy
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_epsilon_dissipation_rate import (
    OneOf_GradientSchemesGrad_epsilonDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_internal_energy import (
    OneOf_GradientSchemesGrad_internalEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_nu_tilda import OneOf_GradientSchemesGrad_nuTilda
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_omega_dissipation_rate import (
    OneOf_GradientSchemesGrad_omegaDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_pressure import OneOf_GradientSchemesGrad_pressure
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_pressure_rgh import (
    OneOf_GradientSchemesGrad_pressureRgh,
)
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_rhok import OneOf_GradientSchemesGrad_rhok
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_temperature import (
    OneOf_GradientSchemesGrad_temperature,
)
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_turbulent_kinetic_energy import (
    OneOf_GradientSchemesGrad_turbulentKineticEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__gradient_schemes_grad_velocity import OneOf_GradientSchemesGrad_velocity


class GradientSchemes(SimScaleModel):
    for_default: OneOf_GradientSchemesForDefault | None = Field(
        validation_alias="forDefault", serialization_alias="forDefault", default=None
    )
    grad_pressure: OneOf_GradientSchemesGrad_pressure | None = Field(default=None)
    grad_velocity: OneOf_GradientSchemesGrad_velocity | None = Field(default=None)
    grad_pressure_rgh: OneOf_GradientSchemesGrad_pressureRgh | None = Field(
        validation_alias="grad_pressureRgh", serialization_alias="grad_pressureRgh", default=None
    )
    grad_density: OneOf_GradientSchemesGrad_density | None = Field(default=None)
    grad_enthalpy: OneOf_GradientSchemesGrad_enthalpy | None = Field(default=None)
    grad_internal_energy: OneOf_GradientSchemesGrad_internalEnergy | None = Field(
        validation_alias="grad_internalEnergy", serialization_alias="grad_internalEnergy", default=None
    )
    grad_turbulent_kinetic_energy: OneOf_GradientSchemesGrad_turbulentKineticEnergy | None = Field(
        validation_alias="grad_turbulentKineticEnergy", serialization_alias="grad_turbulentKineticEnergy", default=None
    )
    grad_epsilon_dissipation_rate: OneOf_GradientSchemesGrad_epsilonDissipationRate | None = Field(
        validation_alias="grad_epsilonDissipationRate", serialization_alias="grad_epsilonDissipationRate", default=None
    )
    grad_omega_dissipation_rate: OneOf_GradientSchemesGrad_omegaDissipationRate | None = Field(
        validation_alias="grad_omegaDissipationRate", serialization_alias="grad_omegaDissipationRate", default=None
    )
    grad_nu_tilda: OneOf_GradientSchemesGrad_nuTilda | None = Field(
        validation_alias="grad_nuTilda", serialization_alias="grad_nuTilda", default=None
    )
    grad_temperature: OneOf_GradientSchemesGrad_temperature | None = Field(default=None)
    grad_rhok: OneOf_GradientSchemesGrad_rhok | None = Field(default=None)
