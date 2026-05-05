from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__electric_resistivity import (
    DimensionalFunction_ElectricResistivity,
)


class IsotropicElectricConductivity(SimScaleModel):
    """Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC_ELECTRIC_CONDUCTIVITY",
        description="Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent.  Schema name: IsotropicElectricConductivity",
    )
    electric_resistivity_function: DimensionalFunction_ElectricResistivity | None = Field(
        validation_alias="electricResistivityFunction", serialization_alias="electricResistivityFunction", default=None
    )
