from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
from simscale_sdk_v1.models.simulation.mean_age_of_fluid_result_type import MeanAgeOfFluidResultType


class FieldCalculationsMeanAgeOfFluidResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AGE_OF_FLUID",
        description="Schema name: FieldCalculationsMeanAgeOfFluidResultControl",
    )
    name: str | None = Field(default=None)
    result_type: MeanAgeOfFluidResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
    age_of_fluid_diffusion: bool | None = Field(
        validation_alias="ageOfFluidDiffusion",
        serialization_alias="ageOfFluidDiffusion",
        default=None,
        description="Enable or disable the diffusion term in the age of fluid equation. The exclusion of the diffusion term can be valid for laminar flows but tends to overestimate the age of fluid for turbulent flows.",
    )
    turbulent_schmidt_number: float | None = Field(
        validation_alias="turbulentSchmidtNumber",
        serialization_alias="turbulentSchmidtNumber",
        default=0.7,
        description="The turbulent Schmidt number characteristic of the flow. For HVAC applications it is recommended to maintain the default value of 0.7.",
    )
    diffusion_coefficient: Dimensional_KinematicViscosity | None = Field(
        validation_alias="diffusionCoefficient", serialization_alias="diffusionCoefficient", default=None
    )
