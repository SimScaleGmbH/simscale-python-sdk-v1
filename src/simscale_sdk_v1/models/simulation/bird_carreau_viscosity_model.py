from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class BirdCarreauViscosityModel(SimScaleModel):
    """Choose between Newtonian and Non-Newtonian viscosity models."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BIRD_CARREAU",
        description="Choose between Newtonian and Non-Newtonian viscosity models.  Schema name: BirdCarreauViscosityModel",
    )
    nu0: Dimensional_KinematicViscosity | None = Field(default=None)
    nu_inf: Dimensional_KinematicViscosity | None = Field(
        validation_alias="nuInf", serialization_alias="nuInf", default=None
    )
    k: Dimensional_Time | None = Field(default=None)
    n: Dimensional_Dimensionless | None = Field(default=None)
    a: Dimensional_Dimensionless | None = Field(default=None)
