from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__mass import Dimensional_Mass


class MassFromDensity(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MASS_FROM_DENSITY",
        description="Schema name: MassFromDensity",
    )
    added_mass: Dimensional_Mass | None = Field(
        validation_alias="addedMass", serialization_alias="addedMass", default=None
    )
