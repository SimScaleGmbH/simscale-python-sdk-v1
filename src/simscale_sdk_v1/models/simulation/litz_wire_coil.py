from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__litz_wire_coil_strand_cross_section_type import (
    OneOf_LitzWireCoilStrandCrossSectionType,
)


class LitzWireCoil(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="LITZ_WIRE_COIL",
        description="Schema name: LitzWireCoil",
    )
    strand_cross_section_type: OneOf_LitzWireCoilStrandCrossSectionType | None = Field(
        validation_alias="strandCrossSectionType", serialization_alias="strandCrossSectionType", default=None
    )
    number_of_turns: int | None = Field(
        validation_alias="numberOfTurns",
        serialization_alias="numberOfTurns",
        default=1,
        description="The Number of Turns option indicates the number of times the wire is wound around the coil's core to form loops. Each loop is a complete 360-degree winding of the wire around the core.",
    )
    number_of_strands_per_turn: int | None = Field(
        validation_alias="numberOfStrandsPerTurn", serialization_alias="numberOfStrandsPerTurn", default=1
    )
