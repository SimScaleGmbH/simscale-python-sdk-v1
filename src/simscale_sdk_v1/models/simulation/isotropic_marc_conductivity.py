from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_conductivity import (
    DimensionalFunction_ThermalConductivity,
)


class IsotropicMarcConductivity(SimScaleModel):
    """Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC",
        description="Define the directional dependency of this property. Isotropic means directionally independent. Orthotropic means directionally dependent.  Schema name: IsotropicMarcConductivity",
    )
    thermal_conductivity: DimensionalFunction_ThermalConductivity | None = Field(
        validation_alias="thermalConductivity", serialization_alias="thermalConductivity", default=None
    )
