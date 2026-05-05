from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.mesh_operation_compute_resource import MeshOperationComputeResource
from simscale_sdk_v1.models.status import Status


class SlimMeshOperation(SimScaleModel):
    mesh_operation_id: str | None = Field(
        validation_alias="meshOperationId",
        serialization_alias="meshOperationId",
        default=None,
        description="The mesh operation ID.",
    )
    name: str | None = Field(default=None, description="The name of the mesh operation.")
    started_at: datetime | None = Field(
        validation_alias="startedAt",
        serialization_alias="startedAt",
        default=None,
        description="The time the mesh operation was started.",
    )
    finished_at: datetime | None = Field(
        validation_alias="finishedAt",
        serialization_alias="finishedAt",
        default=None,
        description="The time the mesh operation was finished.",
    )
    compute_resource: MeshOperationComputeResource | None = Field(
        validation_alias="computeResource", serialization_alias="computeResource", default=None
    )
    status: Status | None = Field(default=None)
    progress: float | None = Field(
        default=None, description="The current progress while the mesh operation is in progress."
    )
    mesh_id: str | None = Field(
        validation_alias="meshId",
        serialization_alias="meshId",
        default=None,
        description="The ID of the generated mesh.",
    )
