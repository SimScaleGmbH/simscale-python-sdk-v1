from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__density import DimensionalFunction_Density


class IsotropicDensityMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC_DENSITY_METHOD",
        description="Schema name: IsotropicDensityMethod",
    )
    density: DimensionalFunction_Density | None = Field(default=None)
