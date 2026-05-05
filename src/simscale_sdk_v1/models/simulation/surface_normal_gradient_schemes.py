from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_for_default import (
    OneOf_SurfaceNormalGradientSchemesForDefault,
)
from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_pressure_rgh import (
    OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_pressureRgh,
)
from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_rho import (
    OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rho,
)
from simscale_sdk_v1.models.simulation.one_of__surface_normal_gradient_schemes_surface_normal_gradient_rhok import (
    OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rhok,
)


class SurfaceNormalGradientSchemes(SimScaleModel):
    for_default: OneOf_SurfaceNormalGradientSchemesForDefault | None = Field(
        validation_alias="forDefault", serialization_alias="forDefault", default=None
    )
    surface_normal_gradient_rho: OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rho | None = Field(
        validation_alias="surfaceNormalGradient_rho", serialization_alias="surfaceNormalGradient_rho", default=None
    )
    surface_normal_gradient_pressure_rgh: OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_pressureRgh | None = (
        Field(
            validation_alias="surfaceNormalGradient_pressureRgh",
            serialization_alias="surfaceNormalGradient_pressureRgh",
            default=None,
        )
    )
    surface_normal_gradient_rhok: OneOf_SurfaceNormalGradientSchemesSurfaceNormalGradient_rhok | None = Field(
        validation_alias="surfaceNormalGradient_rhok", serialization_alias="surfaceNormalGradient_rhok", default=None
    )
