from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__eddy_viscosity_gradient import Dimensional_EddyViscosityGradient


class FixedGradientDVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_GRADIENT",
        description="Schema name: FixedGradientDVBC",
    )
    gradient: Dimensional_EddyViscosityGradient | None = Field(default=None)
