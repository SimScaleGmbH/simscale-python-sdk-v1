from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__dynamic_viscosity import Dimensional_DynamicViscosity
from simscale_sdk_v1.models.simulation.dimensional__temperature import Dimensional_Temperature


class SutherlandViscosity(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SUTHERLAND_VISCOSITY",
        description="Schema name: SutherlandViscosity",
    )
    reference_viscosity: Dimensional_DynamicViscosity | None = Field(
        validation_alias="referenceViscosity", serialization_alias="referenceViscosity", default=None
    )
    reference_temperature: Dimensional_Temperature | None = Field(
        validation_alias="referenceTemperature", serialization_alias="referenceTemperature", default=None
    )
    ts: Dimensional_Temperature | None = Field(default=None)
