from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SimmetrixCellZones(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SIMMETRIX_CELL_ZONES",
        description="Schema name: SimmetrixCellZones",
    )
    name: str | None = Field(default="Zone")
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
