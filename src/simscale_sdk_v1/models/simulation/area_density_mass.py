from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__mass_area_density import Dimensional_MassAreaDensity


class AreaDensityMass(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="AREA_DENSITY_MASS",
        description="Schema name: AreaDensityMass",
    )
    mass: Dimensional_MassAreaDensity | None = Field(default=None)
