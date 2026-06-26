from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ElectromagneticCircuit(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CIRCUIT",
        description="Schema name: ElectromagneticCircuit",
    )
    object_id: str | None = Field(
        validation_alias="objectId",
        serialization_alias="objectId",
        default=None,
        description="The file definition for the EMWORKS Circuit Netlist specification",
    )
