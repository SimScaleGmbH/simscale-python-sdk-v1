from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.gauss_linear_divergence_scheme import GaussLinearDivergenceScheme
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_enthalpy import (
    OneOf_DivergenceSchemesDiv_Phi_enthalpy,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_epsilon_dissipation_rate import (
    OneOf_DivergenceSchemesDiv_Phi_epsilonDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_internal_energy import (
    OneOf_DivergenceSchemesDiv_Phi_internalEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_kinetic_energy import (
    OneOf_DivergenceSchemesDiv_Phi_kineticEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_nu_tilda import (
    OneOf_DivergenceSchemesDiv_Phi_nuTilda,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_omega_dissipation_rate import (
    OneOf_DivergenceSchemesDiv_Phi_omegaDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_passive_scalar import (
    OneOf_DivergenceSchemesDiv_Phi_passiveScalar,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_r import OneOf_DivergenceSchemesDiv_Phi_R
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_temperature import (
    OneOf_DivergenceSchemesDiv_Phi_temperature,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_turbulent_kinetic_energy import (
    OneOf_DivergenceSchemesDiv_Phi_turbulentKineticEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phi_velocity import (
    OneOf_DivergenceSchemesDiv_Phi_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div__phiv_pressure import (
    OneOf_DivergenceSchemesDiv_Phiv_pressure,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phi__ekp import OneOf_DivergenceSchemesDiv_phi_Ekp
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phi_alpha import (
    OneOf_DivergenceSchemesDiv_phi_alpha,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phid_pressure import (
    OneOf_DivergenceSchemesDiv_phid_pressure,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_phirb_alpha import (
    OneOf_DivergenceSchemesDiv_phirb_alpha,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_r import OneOf_DivergenceSchemesDiv_R
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_rho_phi_velocity import (
    OneOf_DivergenceSchemesDiv_rhoPhi_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_tau_mc import OneOf_DivergenceSchemesDiv_tauMC
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_div_velocity import (
    OneOf_DivergenceSchemesDiv_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__divergence_schemes_for_default import OneOf_DivergenceSchemesForDefault


class DivergenceSchemes(SimScaleModel):
    for_default: OneOf_DivergenceSchemesForDefault | None = Field(
        validation_alias="forDefault", serialization_alias="forDefault", default=None
    )
    div__phi_velocity: OneOf_DivergenceSchemesDiv_Phi_velocity | None = Field(
        validation_alias="div_Phi_velocity", serialization_alias="div_Phi_velocity", default=None
    )
    div__phi_kinetic_energy: OneOf_DivergenceSchemesDiv_Phi_kineticEnergy | None = Field(
        validation_alias="div_Phi_kineticEnergy", serialization_alias="div_Phi_kineticEnergy", default=None
    )
    div__phi_enthalpy: OneOf_DivergenceSchemesDiv_Phi_enthalpy | None = Field(
        validation_alias="div_Phi_enthalpy", serialization_alias="div_Phi_enthalpy", default=None
    )
    div__phi_internal_energy: OneOf_DivergenceSchemesDiv_Phi_internalEnergy | None = Field(
        validation_alias="div_Phi_internalEnergy", serialization_alias="div_Phi_internalEnergy", default=None
    )
    div__phiv_pressure: OneOf_DivergenceSchemesDiv_Phiv_pressure | None = Field(
        validation_alias="div_Phiv_pressure", serialization_alias="div_Phiv_pressure", default=None
    )
    div__phi_turbulent_kinetic_energy: OneOf_DivergenceSchemesDiv_Phi_turbulentKineticEnergy | None = Field(
        validation_alias="div_Phi_turbulentKineticEnergy",
        serialization_alias="div_Phi_turbulentKineticEnergy",
        default=None,
    )
    div__nu_eff_dev_t_grad_velocity: GaussLinearDivergenceScheme | None = Field(
        validation_alias="div_NuEff_dev_T_grad_velocity",
        serialization_alias="div_NuEff_dev_T_grad_velocity",
        default=None,
    )
    div__mu_eff_dev2_t_grad_velocity: GaussLinearDivergenceScheme | None = Field(
        validation_alias="div_MuEff_dev2_T_grad_velocity",
        serialization_alias="div_MuEff_dev2_T_grad_velocity",
        default=None,
    )
    div__phi_omega_dissipation_rate: OneOf_DivergenceSchemesDiv_Phi_omegaDissipationRate | None = Field(
        validation_alias="div_Phi_omegaDissipationRate",
        serialization_alias="div_Phi_omegaDissipationRate",
        default=None,
    )
    div__phi_epsilon_dissipation_rate: OneOf_DivergenceSchemesDiv_Phi_epsilonDissipationRate | None = Field(
        validation_alias="div_Phi_epsilonDissipationRate",
        serialization_alias="div_Phi_epsilonDissipationRate",
        default=None,
    )
    div_r: OneOf_DivergenceSchemesDiv_R | None = Field(
        validation_alias="div_R", serialization_alias="div_R", default=None
    )
    div__phi_r: OneOf_DivergenceSchemesDiv_Phi_R | None = Field(
        validation_alias="div_Phi_R", serialization_alias="div_Phi_R", default=None
    )
    div__phi_nu_tilda: OneOf_DivergenceSchemesDiv_Phi_nuTilda | None = Field(
        validation_alias="div_Phi_nuTilda", serialization_alias="div_Phi_nuTilda", default=None
    )
    div__phi_temperature: OneOf_DivergenceSchemesDiv_Phi_temperature | None = Field(
        validation_alias="div_Phi_temperature", serialization_alias="div_Phi_temperature", default=None
    )
    div__phi_passive_scalar: OneOf_DivergenceSchemesDiv_Phi_passiveScalar | None = Field(
        validation_alias="div_Phi_passiveScalar", serialization_alias="div_Phi_passiveScalar", default=None
    )
    div_tau_mc: OneOf_DivergenceSchemesDiv_tauMC | None = Field(
        validation_alias="div_tauMC", serialization_alias="div_tauMC", default=None
    )
    div_phid_pressure: OneOf_DivergenceSchemesDiv_phid_pressure | None = Field(default=None)
    div_velocity: OneOf_DivergenceSchemesDiv_velocity | None = Field(default=None)
    div_phi__ekp: OneOf_DivergenceSchemesDiv_phi_Ekp | None = Field(
        validation_alias="div_phi_Ekp", serialization_alias="div_phi_Ekp", default=None
    )
    div_phirb_alpha: OneOf_DivergenceSchemesDiv_phirb_alpha | None = Field(default=None)
    div_mu_eff_dev_t_grad_velocity: GaussLinearDivergenceScheme | None = Field(
        validation_alias="div_muEff_dev_T_grad_velocity",
        serialization_alias="div_muEff_dev_T_grad_velocity",
        default=None,
    )
    div_phi_alpha: OneOf_DivergenceSchemesDiv_phi_alpha | None = Field(default=None)
    div_rho_phi_velocity: OneOf_DivergenceSchemesDiv_rhoPhi_velocity | None = Field(
        validation_alias="div_rhoPhi_velocity", serialization_alias="div_rhoPhi_velocity", default=None
    )
