from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
from simscale_sdk_v1.models.simulation.dimensional_function__dynamic_viscosity import (
    DimensionalFunction_DynamicViscosity,
)
from simscale_sdk_v1.models.simulation.dimensional_function__kinematic_viscosity import (
    DimensionalFunction_KinematicViscosity,
)


class NewtonianViscosityModel(SimScaleModel):
    """Choose between Newtonian and Non-Newtonian viscosity models."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="NEWTONIAN",
        description="Choose between Newtonian and Non-Newtonian viscosity models.  Schema name: NewtonianViscosityModel",
    )
    kinematic_viscosity: Dimensional_KinematicViscosity | None = Field(
        validation_alias="kinematicViscosity", serialization_alias="kinematicViscosity", default=None
    )
    kinematic_viscosity_function: DimensionalFunction_KinematicViscosity | None = Field(
        validation_alias="kinematicViscosityFunction", serialization_alias="kinematicViscosityFunction", default=None
    )
    dynamic_viscosity_function: DimensionalFunction_DynamicViscosity | None = Field(
        validation_alias="dynamicViscosityFunction", serialization_alias="dynamicViscosityFunction", default=None
    )
