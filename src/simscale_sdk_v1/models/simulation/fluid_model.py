from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
from simscale_sdk_v1.models.simulation.dimensional__surface_tension import Dimensional_SurfaceTension
from simscale_sdk_v1.models.simulation.dimensional_vector__acceleration import DimensionalVector_Acceleration
from simscale_sdk_v1.models.simulation.one_of__fluid_model_delta_coefficient import OneOf_FluidModelDeltaCoefficient


class FluidModel(SimScaleModel):
    turbulent_schmidt_number: float | None = Field(
        validation_alias="turbulentSchmidtNumber", serialization_alias="turbulentSchmidtNumber", default=0.7
    )
    diffusion_coefficients: list[Dimensional_KinematicViscosity] | None = Field(
        validation_alias="diffusionCoefficients", serialization_alias="diffusionCoefficients", default=None
    )
    delta_coefficient: OneOf_FluidModelDeltaCoefficient | None = Field(
        validation_alias="deltaCoefficient", serialization_alias="deltaCoefficient", default=None
    )
    gravity: DimensionalVector_Acceleration | None = Field(default=None)
    surface_tension: Dimensional_SurfaceTension | None = Field(
        validation_alias="surfaceTension", serialization_alias="surfaceTension", default=None
    )
