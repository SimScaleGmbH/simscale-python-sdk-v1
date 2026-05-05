from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity


class PowerLawViscosityModel(SimScaleModel):
    """Choose between Newtonian and Non-Newtonian viscosity models."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="POWER_LAW",
        description="Choose between Newtonian and Non-Newtonian viscosity models.  Schema name: PowerLawViscosityModel",
    )
    k: Dimensional_KinematicViscosity | None = Field(default=None)
    n: Dimensional_Dimensionless | None = Field(default=None)
    nu_min: Dimensional_KinematicViscosity | None = Field(
        validation_alias="nuMin", serialization_alias="nuMin", default=None
    )
    nu_max: Dimensional_KinematicViscosity | None = Field(
        validation_alias="nuMax", serialization_alias="nuMax", default=None
    )
