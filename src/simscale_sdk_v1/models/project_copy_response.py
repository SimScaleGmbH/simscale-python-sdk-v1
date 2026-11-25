from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_entry import LogEntry
from simscale_sdk_v1.models.status import Status


class ProjectCopyResponse(SimScaleModel):
    project_copy_id: str = Field(
        validation_alias="projectCopyId",
        serialization_alias="projectCopyId",
        description="The ID of the project copy operation.",
    )
    status: Status
    project_id: str | None = Field(
        validation_alias="projectId",
        serialization_alias="projectId",
        default=None,
        description="The ID of the new project when the copy succeeded.",
    )
    failure_reason: LogEntry | None = Field(
        validation_alias="failureReason", serialization_alias="failureReason", default=None
    )
