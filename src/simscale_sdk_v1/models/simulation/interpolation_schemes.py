from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_for_default import (
    OneOf_InterpolationSchemesForDefault,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate__hby_a import (
    OneOf_InterpolationSchemesInterpolate_HbyA,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_grad_enthalpy import (
    OneOf_InterpolationSchemesInterpolate_grad_enthalpy,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_kappa import (
    OneOf_InterpolationSchemesInterpolate_kappa,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_map__kappa import (
    OneOf_InterpolationSchemesInterpolate_map_Kappa,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_r_au import (
    OneOf_InterpolationSchemesInterpolate_rAU,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho import (
    OneOf_InterpolationSchemesInterpolate_rho,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho_0_velocity0 import (
    OneOf_InterpolationSchemesInterpolate_rho_0_velocity0,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho__hbya import (
    OneOf_InterpolationSchemesInterpolate_rho_Hbya,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_rho_r_au import (
    OneOf_InterpolationSchemesInterpolate_rho_rAU,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_thermo_rho__cp import (
    OneOf_InterpolationSchemesInterpolate_thermo_rho_Cp,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_velocity import (
    OneOf_InterpolationSchemesInterpolate_velocity,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_interpolate_velocity0 import (
    OneOf_InterpolationSchemesInterpolate_velocity0,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_rho import (
    OneOf_InterpolationSchemesReconstruct_rho,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_temperature import (
    OneOf_InterpolationSchemesReconstruct_temperature,
)
from simscale_sdk_v1.models.simulation.one_of__interpolation_schemes_reconstruct_velocity import (
    OneOf_InterpolationSchemesReconstruct_velocity,
)


class InterpolationSchemes(SimScaleModel):
    for_default: OneOf_InterpolationSchemesForDefault | None = Field(
        validation_alias="forDefault", serialization_alias="forDefault", default=None
    )
    interpolate__hby_a: OneOf_InterpolationSchemesInterpolate_HbyA | None = Field(
        validation_alias="interpolate_HbyA", serialization_alias="interpolate_HbyA", default=None
    )
    interpolate_velocity: OneOf_InterpolationSchemesInterpolate_velocity | None = Field(default=None)
    interpolate_kappa: OneOf_InterpolationSchemesInterpolate_kappa | None = Field(default=None)
    interpolate_rho: OneOf_InterpolationSchemesInterpolate_rho | None = Field(default=None)
    interpolate_thermo_rho__cp: OneOf_InterpolationSchemesInterpolate_thermo_rho_Cp | None = Field(
        validation_alias="interpolate_thermo_rho_Cp", serialization_alias="interpolate_thermo_rho_Cp", default=None
    )
    interpolate_map__kappa: OneOf_InterpolationSchemesInterpolate_map_Kappa | None = Field(
        validation_alias="interpolate_map_Kappa", serialization_alias="interpolate_map_Kappa", default=None
    )
    interpolate_rho__hbya: OneOf_InterpolationSchemesInterpolate_rho_Hbya | None = Field(
        validation_alias="interpolate_rho_Hbya", serialization_alias="interpolate_rho_Hbya", default=None
    )
    interpolate_rho_0_velocity0: OneOf_InterpolationSchemesInterpolate_rho_0_velocity0 | None = Field(default=None)
    interpolate_grad_enthalpy: OneOf_InterpolationSchemesInterpolate_grad_enthalpy | None = Field(default=None)
    interpolate_rho_r_au: OneOf_InterpolationSchemesInterpolate_rho_rAU | None = Field(
        validation_alias="interpolate_rho_rAU", serialization_alias="interpolate_rho_rAU", default=None
    )
    interpolate_r_au: OneOf_InterpolationSchemesInterpolate_rAU | None = Field(
        validation_alias="interpolate_rAU", serialization_alias="interpolate_rAU", default=None
    )
    interpolate_velocity0: OneOf_InterpolationSchemesInterpolate_velocity0 | None = Field(default=None)
    reconstruct_velocity: OneOf_InterpolationSchemesReconstruct_velocity | None = Field(default=None)
    reconstruct_temperature: OneOf_InterpolationSchemesReconstruct_temperature | None = Field(default=None)
    reconstruct_rho: OneOf_InterpolationSchemesReconstruct_rho | None = Field(default=None)
