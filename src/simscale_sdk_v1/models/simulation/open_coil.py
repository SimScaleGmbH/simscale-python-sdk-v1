from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class OpenCoil(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="OPEN_COIL", description="Schema name: OpenCoil"
    )
    bodies: TopologicalReference | None = Field(default=None)
    entry_port: TopologicalReference | None = Field(
        validation_alias="entryPort", serialization_alias="entryPort", default=None
    )
    exit_port: TopologicalReference | None = Field(
        validation_alias="exitPort", serialization_alias="exitPort", default=None
    )
