from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__contact_resistance import Dimensional_ContactResistance
from simscale_sdk_v1.models.simulation.dimensional__electric_resistance import Dimensional_ElectricResistance


class TotalResistanceInterfaceThermal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_RESISTANCE",
        description="Schema name: TotalResistanceInterfaceThermal",
    )
    contact_resistance: Dimensional_ContactResistance | None = Field(
        validation_alias="contactResistance", serialization_alias="contactResistance", default=None
    )
    electric_resistance: Dimensional_ElectricResistance | None = Field(
        validation_alias="electricResistance", serialization_alias="electricResistance", default=None
    )
