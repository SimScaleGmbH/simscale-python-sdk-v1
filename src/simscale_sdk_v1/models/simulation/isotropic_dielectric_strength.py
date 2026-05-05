from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__electric_field_strength import (
    DimensionalFunction_ElectricFieldStrength,
)


class IsotropicDielectricStrength(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Schema name: IsotropicDielectricStrength",
    )
    dielectric_strength: DimensionalFunction_ElectricFieldStrength | None = Field(
        validation_alias="dielectricStrength", serialization_alias="dielectricStrength", default=None
    )
