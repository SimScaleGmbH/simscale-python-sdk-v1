from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Mesh(SimScaleModel):
    mesh_id: str | None = Field(
        validation_alias="meshId", serialization_alias="meshId", default=None, description="The ID of the mesh."
    )
    name: str | None = Field(default=None, description="The name of the mesh.")
    created_at: datetime | None = Field(
        validation_alias="createdAt",
        serialization_alias="createdAt",
        default=None,
        description="The time when the mesh was imported.",
    )
    number_of_cells: int | None = Field(
        validation_alias="numberOfCells",
        serialization_alias="numberOfCells",
        default=None,
        description="Number of cells of the mesh.",
    )
    number_of_nodes: int | None = Field(
        validation_alias="numberOfNodes",
        serialization_alias="numberOfNodes",
        default=None,
        description="Number of nodes of the mesh.",
    )
