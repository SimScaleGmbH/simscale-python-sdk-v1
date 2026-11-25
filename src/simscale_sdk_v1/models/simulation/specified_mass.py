from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__mass import Dimensional_Mass


class SpecifiedMass(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIFIED_MASS",
        description="Schema name: SpecifiedMass",
    )
    mass: Dimensional_Mass | None = Field(default=None)
