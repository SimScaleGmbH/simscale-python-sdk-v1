from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__contact_resistance import Dimensional_ContactResistance


class TotalResistanceWallThermal(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_RESISTANCE",
        description="Schema name: TotalResistanceWallThermal",
    )
    contact_resistance: Dimensional_ContactResistance | None = Field(
        validation_alias="contactResistance", serialization_alias="contactResistance", default=None
    )
