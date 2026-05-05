from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__specific_heat import DimensionalFunction_SpecificHeat


class IsotropicSpecificHeatMethod(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="ISOTROPIC_SPECIFIC_HEAT_METHOD",
        description="Schema name: IsotropicSpecificHeatMethod",
    )
    specific_heat: DimensionalFunction_SpecificHeat | None = Field(
        validation_alias="specificHeat", serialization_alias="specificHeat", default=None
    )
