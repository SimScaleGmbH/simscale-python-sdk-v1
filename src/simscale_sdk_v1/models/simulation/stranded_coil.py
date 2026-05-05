from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class StrandedCoil(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRANDED_COIL",
        description="Schema name: StrandedCoil",
    )
    number_of_turns: int | None = Field(
        validation_alias="numberOfTurns",
        serialization_alias="numberOfTurns",
        default=1,
        description="The Number of Turns option indicates the number of times the wire is wound around the coil's core to form loops. Each loop is a complete 360-degree winding of the wire around the core.",
    )
    wire_diameter: Dimensional_Length | None = Field(
        validation_alias="wireDiameter", serialization_alias="wireDiameter", default=None
    )
