from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__specific_contact_resistance import (
    Dimensional_SpecificContactResistance,
)
from simscale_sdk_v1.models.simulation.dimensional__specific_electric_resistance import (
    Dimensional_SpecificElectricResistance,
)


class SpecificResistanceInterfaceThermal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SPECIFIC_RESISTANCE",
        description="Schema name: SpecificResistanceInterfaceThermal",
    )
    contact_resistance: Dimensional_SpecificContactResistance | None = Field(
        validation_alias="contactResistance", serialization_alias="contactResistance", default=None
    )
    electric_resistance: Dimensional_SpecificElectricResistance | None = Field(
        validation_alias="electricResistance", serialization_alias="electricResistance", default=None
    )
