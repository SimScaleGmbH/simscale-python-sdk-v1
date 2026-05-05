from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__electric_resistivity import (
    DimensionalFunction_ElectricResistivity,
)


class OrthotropicElectricConductivity(SimScaleModel):
    """Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ORTHOTROPIC_ELECTRIC_CONDUCTIVITY",
        description="Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent.  Schema name: OrthotropicElectricConductivity",
    )
    electric_resistivity_x: DimensionalFunction_ElectricResistivity | None = Field(
        validation_alias="electricResistivityX", serialization_alias="electricResistivityX", default=None
    )
    electric_resistivity_y: DimensionalFunction_ElectricResistivity | None = Field(
        validation_alias="electricResistivityY", serialization_alias="electricResistivityY", default=None
    )
    electric_resistivity_z: DimensionalFunction_ElectricResistivity | None = Field(
        validation_alias="electricResistivityZ", serialization_alias="electricResistivityZ", default=None
    )
