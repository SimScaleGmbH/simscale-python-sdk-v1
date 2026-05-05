from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__thermal_conductivity import (
    DimensionalFunction_ThermalConductivity,
)


class CrossPlaneOrthotropicConductivity(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CROSS_PLANE_ORTHOTROPIC",
        description="Schema name: CrossPlaneOrthotropicConductivity",
    )
    in_plane_conductivity: DimensionalFunction_ThermalConductivity | None = Field(
        validation_alias="inPlaneConductivity", serialization_alias="inPlaneConductivity", default=None
    )
    cross_plane_conductivity: DimensionalFunction_ThermalConductivity | None = Field(
        validation_alias="crossPlaneConductivity", serialization_alias="crossPlaneConductivity", default=None
    )
