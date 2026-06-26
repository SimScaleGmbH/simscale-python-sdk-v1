from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class InitializeWorkflowRunRequest(SimScaleModel):
    """Workflow run information to be presented for the initialization."""

    workflow_run_mode: Literal["DRY", "REAL"] = Field(
        validation_alias="workflowRunMode", serialization_alias="workflowRunMode"
    )
    workflow_run_name: str | None = Field(
        validation_alias="workflowRunName", serialization_alias="workflowRunName", default=None
    )
    workflow_version_id: str = Field(
        validation_alias="workflowVersionId",
        serialization_alias="workflowVersionId",
        default=None,
        description="Workflow version identifier. It is a string composed of the type identifier and a UUID: `workflow.version:[UUID]`.",
    )
