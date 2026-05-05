from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.divergence_schemes import DivergenceSchemes
from simscale_sdk_v1.models.simulation.flux_schemes import FluxSchemes
from simscale_sdk_v1.models.simulation.gradient_schemes import GradientSchemes
from simscale_sdk_v1.models.simulation.interpolation_schemes import InterpolationSchemes
from simscale_sdk_v1.models.simulation.laplacian_schemes import LaplacianSchemes
from simscale_sdk_v1.models.simulation.spatial_discretization_schemes import SpatialDiscretizationSchemes
from simscale_sdk_v1.models.simulation.surface_normal_gradient_schemes import SurfaceNormalGradientSchemes
from simscale_sdk_v1.models.simulation.time_differentiation_schemes import TimeDifferentiationSchemes


class Schemes(SimScaleModel):
    flux: FluxSchemes | None = Field(default=None)
    time_differentiation: TimeDifferentiationSchemes | None = Field(
        validation_alias="timeDifferentiation", serialization_alias="timeDifferentiation", default=None
    )
    spatial_discretization: SpatialDiscretizationSchemes | None = Field(
        validation_alias="spatialDiscretization", serialization_alias="spatialDiscretization", default=None
    )
    gradient: GradientSchemes | None = Field(default=None)
    divergence: DivergenceSchemes | None = Field(default=None)
    laplacian: LaplacianSchemes | None = Field(default=None)
    interpolation: InterpolationSchemes | None = Field(default=None)
    surface_normal_gradient: SurfaceNormalGradientSchemes | None = Field(
        validation_alias="surfaceNormalGradient", serialization_alias="surfaceNormalGradient", default=None
    )
    second_order_convection: bool | None = Field(
        validation_alias="secondOrderConvection",
        serialization_alias="secondOrderConvection",
        default=False,
        description="Whether to use second-order convection scheme, which is less stable but more accurate for a given mesh. If false, first-order accurate upwind scheme is used.",
    )
