from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.mesh_operation_compute_resource import MeshOperationComputeResource
from simscale_sdk_v1.models.meshing.algorithm import Algorithm
from simscale_sdk_v1.models.status import Status


class MeshOperation(SimScaleModel):
    mesh_operation_id: str | None = Field(
        validation_alias="meshOperationId",
        serialization_alias="meshOperationId",
        default=None,
        description="The mesh operation ID.",
    )
    name: str = Field(description="The name of the mesh operation.")
    version: str = Field(
        default="10.0",
        description="The schema version of the mesh operation. This can be either the external version like `8.0`, or the internal version like `internal:53`.",
    )
    cad_id: str = Field(
        validation_alias="cadId", serialization_alias="cadId", description="The ID of CAD input to the mesh operation."
    )
    state_id: str = Field(
        validation_alias="stateId",
        serialization_alias="stateId",
        description="The ID of CAD state input to the mesh operation.",
    )
    model: Algorithm
    created_at: datetime | None = Field(
        validation_alias="createdAt",
        serialization_alias="createdAt",
        default=None,
        description="The time the mesh operation was created.",
    )
    modified_at: datetime | None = Field(
        validation_alias="modifiedAt",
        serialization_alias="modifiedAt",
        default=None,
        description="The time the mesh operation was last modified.",
    )
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
