from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dimensionless import Dimensional_Dimensionless
from simscale_sdk_v1.models.simulation.dimensional__kinematic_viscosity import Dimensional_KinematicViscosity
from simscale_sdk_v1.models.simulation.dimensional__turbulence_kinetic_energy import Dimensional_TurbulenceKineticEnergy


class HerschelBulkleyViscosityModel(SimScaleModel):
    """Choose between Newtonian and Non-Newtonian viscosity models."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="HERSCHEL_BULKLEY",
        description="Choose between Newtonian and Non-Newtonian viscosity models.  Schema name: HerschelBulkleyViscosityModel",
    )
    k: Dimensional_KinematicViscosity | None = Field(default=None)
    n: Dimensional_Dimensionless | None = Field(default=None)
    tau0: Dimensional_TurbulenceKineticEnergy | None = Field(default=None)
    nu0: Dimensional_KinematicViscosity | None = Field(default=None)
