from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__specific_heat import DimensionalFunction_SpecificHeat
from simscale_sdk_v1.models.simulation.one_of__marc_thermal_properties_conductivity import (
    OneOf_MarcThermalPropertiesConductivity,
)


class MarcThermalProperties(SimScaleModel):
    conductivity: OneOf_MarcThermalPropertiesConductivity | None = Field(default=None)
    specific_heat: DimensionalFunction_SpecificHeat | None = Field(
        validation_alias="specificHeat", serialization_alias="specificHeat", default=None
    )
