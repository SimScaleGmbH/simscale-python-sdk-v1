from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ResourceToMove(SimScaleModel):
    """Specify the resource to be moved. One of `folderId` or `projectId` must be defined. An error is returned if both fields are passed."""

    folder_id: str | None = Field(
        validation_alias="folderId",
        serialization_alias="folderId",
        default=None,
        description="Use this field to move an entire folder",
    )
    project_id: str | None = Field(
        validation_alias="projectId",
        serialization_alias="projectId",
        default=None,
        description="Use this field to move a project",
    )
