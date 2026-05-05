from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_for_default import OneOf_LaplacianSchemesForDefault
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_1_a_u_pressure import (
    OneOf_LaplacianSchemesLaplacian_1A_U_pressure,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__depsilon_eff_epsilon_dissipation_rate import (
    OneOf_LaplacianSchemesLaplacian_DepsilonEff_epsilonDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dk_eff_turbulent_kinetic_energy import (
    OneOf_LaplacianSchemesLaplacian_DkEff_turbulentKineticEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dnu_tilda_eff_nu_tilda import (
    OneOf_LaplacianSchemesLaplacian_DnuTildaEff_nuTilda,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__domega_eff_omega_dissipation_rate import (
    OneOf_LaplacianSchemesLaplacian_DomegaEff_omegaDissipationRate,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__dp_pressure import (
    OneOf_LaplacianSchemesLaplacian_Dp_pressure,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__nu_eff_velocity import (
    OneOf_LaplacianSchemesLaplacian_NuEff_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian__nu_velocity import (
    OneOf_LaplacianSchemesLaplacian_Nu_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_enthalpy import (
    OneOf_LaplacianSchemesLaplacian_alphaEff_enthalpy,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_internal_energy import (
    OneOf_LaplacianSchemesLaplacian_alphaEff_internalEnergy,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_eff_temperature import (
    OneOf_LaplacianSchemesLaplacian_alphaEff_temperature,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_alpha_enthalpy import (
    OneOf_LaplacianSchemesLaplacian_alpha_enthalpy,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_dr_eff_r import (
    OneOf_LaplacianSchemesLaplacian_DREff_R,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_dt_passive_scalar import (
    OneOf_LaplacianSchemesLaplacian_DT_passiveScalar,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_mu_eff_velocity import (
    OneOf_LaplacianSchemesLaplacian_muEff_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_mut_velocity import (
    OneOf_LaplacianSchemesLaplacian_mut_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_r_a_uf_pressure import (
    OneOf_LaplacianSchemesLaplacian_rAUf_pressure,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_r_a_uf_pressure_rgh import (
    OneOf_LaplacianSchemesLaplacian_rAUf_pressureRgh,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rho_1_a_u_pressure import (
    OneOf_LaplacianSchemesLaplacian_rho_1_A_U_pressure,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rhor_a_uf_pressure import (
    OneOf_LaplacianSchemesLaplacian_rhorAUf_pressure,
)
from simscale_sdk_v1.models.simulation.one_of__laplacian_schemes_laplacian_rhor_a_uf_pressure_rgh import (
    OneOf_LaplacianSchemesLaplacian_rhorAUf_pressureRgh,
)


class LaplacianSchemes(SimScaleModel):
    for_default: OneOf_LaplacianSchemesForDefault | None = Field(
        validation_alias="forDefault", serialization_alias="forDefault", default=None
    )
    laplacian__nu_eff_velocity: OneOf_LaplacianSchemesLaplacian_NuEff_velocity | None = Field(
        validation_alias="laplacian_NuEff_velocity", serialization_alias="laplacian_NuEff_velocity", default=None
    )
    laplacian_1_a_u_pressure: OneOf_LaplacianSchemesLaplacian_1A_U_pressure | None = Field(
        validation_alias="laplacian_1A_U_pressure", serialization_alias="laplacian_1A_U_pressure", default=None
    )
    laplacian__nu_velocity: OneOf_LaplacianSchemesLaplacian_Nu_velocity | None = Field(
        validation_alias="laplacian_Nu_velocity", serialization_alias="laplacian_Nu_velocity", default=None
    )
    laplacian_dr_eff_r: OneOf_LaplacianSchemesLaplacian_DREff_R | None = Field(
        validation_alias="laplacian_DREff_R", serialization_alias="laplacian_DREff_R", default=None
    )
    laplacian__dnu_tilda_eff_nu_tilda: OneOf_LaplacianSchemesLaplacian_DnuTildaEff_nuTilda | None = Field(
        validation_alias="laplacian_DnuTildaEff_nuTilda",
        serialization_alias="laplacian_DnuTildaEff_nuTilda",
        default=None,
    )
    laplacian__dk_eff_turbulent_kinetic_energy: OneOf_LaplacianSchemesLaplacian_DkEff_turbulentKineticEnergy | None = (
        Field(
            validation_alias="laplacian_DkEff_turbulentKineticEnergy",
            serialization_alias="laplacian_DkEff_turbulentKineticEnergy",
            default=None,
        )
    )
    laplacian_alpha_eff_enthalpy: OneOf_LaplacianSchemesLaplacian_alphaEff_enthalpy | None = Field(
        validation_alias="laplacian_alphaEff_enthalpy", serialization_alias="laplacian_alphaEff_enthalpy", default=None
    )
    laplacian_alpha_enthalpy: OneOf_LaplacianSchemesLaplacian_alpha_enthalpy | None = Field(default=None)
    laplacian_mu_eff_velocity: OneOf_LaplacianSchemesLaplacian_muEff_velocity | None = Field(
        validation_alias="laplacian_muEff_velocity", serialization_alias="laplacian_muEff_velocity", default=None
    )
    laplacian_alpha_eff_internal_energy: OneOf_LaplacianSchemesLaplacian_alphaEff_internalEnergy | None = Field(
        validation_alias="laplacian_alphaEff_internalEnergy",
        serialization_alias="laplacian_alphaEff_internalEnergy",
        default=None,
    )
    laplacian_rhor_a_uf_pressure_rgh: OneOf_LaplacianSchemesLaplacian_rhorAUf_pressureRgh | None = Field(
        validation_alias="laplacian_rhorAUf_pressureRgh",
        serialization_alias="laplacian_rhorAUf_pressureRgh",
        default=None,
    )
    laplacian__depsilon_eff_epsilon_dissipation_rate: (
        OneOf_LaplacianSchemesLaplacian_DepsilonEff_epsilonDissipationRate | None
    ) = Field(
        validation_alias="laplacian_DepsilonEff_epsilonDissipationRate",
        serialization_alias="laplacian_DepsilonEff_epsilonDissipationRate",
        default=None,
    )
    laplacian__domega_eff_omega_dissipation_rate: (
        OneOf_LaplacianSchemesLaplacian_DomegaEff_omegaDissipationRate | None
    ) = Field(
        validation_alias="laplacian_DomegaEff_omegaDissipationRate",
        serialization_alias="laplacian_DomegaEff_omegaDissipationRate",
        default=None,
    )
    laplacian_r_a_uf_pressure: OneOf_LaplacianSchemesLaplacian_rAUf_pressure | None = Field(
        validation_alias="laplacian_rAUf_pressure", serialization_alias="laplacian_rAUf_pressure", default=None
    )
    laplacian_dt_passive_scalar: OneOf_LaplacianSchemesLaplacian_DT_passiveScalar | None = Field(
        validation_alias="laplacian_DT_passiveScalar", serialization_alias="laplacian_DT_passiveScalar", default=None
    )
    laplacian__dp_pressure: OneOf_LaplacianSchemesLaplacian_Dp_pressure | None = Field(
        validation_alias="laplacian_Dp_pressure", serialization_alias="laplacian_Dp_pressure", default=None
    )
    laplacian_rhor_a_uf_pressure: OneOf_LaplacianSchemesLaplacian_rhorAUf_pressure | None = Field(
        validation_alias="laplacian_rhorAUf_pressure", serialization_alias="laplacian_rhorAUf_pressure", default=None
    )
    laplacian_rho_1_a_u_pressure: OneOf_LaplacianSchemesLaplacian_rho_1_A_U_pressure | None = Field(
        validation_alias="laplacian_rho_1_A_U_pressure",
        serialization_alias="laplacian_rho_1_A_U_pressure",
        default=None,
    )
    laplacian_mut_velocity: OneOf_LaplacianSchemesLaplacian_mut_velocity | None = Field(default=None)
    laplacian_alpha_eff_temperature: OneOf_LaplacianSchemesLaplacian_alphaEff_temperature | None = Field(
        validation_alias="laplacian_alphaEff_temperature",
        serialization_alias="laplacian_alphaEff_temperature",
        default=None,
    )
    laplacian_r_a_uf_pressure_rgh: OneOf_LaplacianSchemesLaplacian_rAUf_pressureRgh | None = Field(
        validation_alias="laplacian_rAUf_pressureRgh", serialization_alias="laplacian_rAUf_pressureRgh", default=None
    )
