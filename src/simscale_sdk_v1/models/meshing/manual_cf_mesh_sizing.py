from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.dimensional__length import Dimensional_Length


class ManualCfMeshSizing(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MANUAL_CF_MESH_SIZING",
        description="Schema name: ManualCfMeshSizing",
    )
    maximum_edge_length: Dimensional_Length | None = Field(
        validation_alias="maximumEdgeLength", serialization_alias="maximumEdgeLength", default=None
    )
    minimum_edge_length: Dimensional_Length | None = Field(
        validation_alias="minimumEdgeLength", serialization_alias="minimumEdgeLength", default=None
    )
