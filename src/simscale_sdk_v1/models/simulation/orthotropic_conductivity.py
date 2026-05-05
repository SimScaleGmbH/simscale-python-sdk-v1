from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_conductivity import (
    DimensionalFunction_ThermalConductivity,
)


class OrthotropicConductivity(SimScaleModel):
    """Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ORTHOTROPIC",
        description="Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent.  Schema name: OrthotropicConductivity",
    )
    thermal_conductivity_x: DimensionalFunction_ThermalConductivity | None = Field(
        validation_alias="thermalConductivityX", serialization_alias="thermalConductivityX", default=None
    )
    thermal_conductivity_y: DimensionalFunction_ThermalConductivity | None = Field(
        validation_alias="thermalConductivityY", serialization_alias="thermalConductivityY", default=None
    )
    thermal_conductivity_z: DimensionalFunction_ThermalConductivity | None = Field(
        validation_alias="thermalConductivityZ", serialization_alias="thermalConductivityZ", default=None
    )
