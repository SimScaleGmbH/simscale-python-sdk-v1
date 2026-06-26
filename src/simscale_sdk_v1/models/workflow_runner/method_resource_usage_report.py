from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflow_runner.resource_usage_summary import ResourceUsageSummary


class MethodResourceUsageReport(SimScaleModel):
    """Standalone resource usage report for one method run."""

    allocated_cpus: int | None = Field(
        validation_alias="allocatedCpus", serialization_alias="allocatedCpus", default=None
    )
    allocated_gpus: int | None = Field(
        validation_alias="allocatedGpus", serialization_alias="allocatedGpus", default=None
    )
    duration_in_millis: int | None = Field(
        validation_alias="durationInMillis", serialization_alias="durationInMillis", default=None
    )
    finished_at: datetime | None = Field(validation_alias="finishedAt", serialization_alias="finishedAt", default=None)
    method_run_id: str | None = Field(
        validation_alias="methodRunId",
        serialization_alias="methodRunId",
        default=None,
        description="Method run identifier. It is a string composed of the type identifier and a UUID: `method.run:[UUID]`.",
    )
    name: str | None = Field(default=None)
    operation_run_id: str | None = Field(
        validation_alias="operationRunId",
        serialization_alias="operationRunId",
        default=None,
        description="Operation run identifier. It is a string composed of the type identifier and a UUID: `operation.run:[UUID]`.",
    )
    project_id: str | None = Field(validation_alias="projectId", serialization_alias="projectId", default=None)
    project_name: str | None = Field(validation_alias="projectName", serialization_alias="projectName", default=None)
    run_terminal_state: str | None = Field(
        validation_alias="runTerminalState", serialization_alias="runTerminalState", default=None
    )
    started_at: datetime | None = Field(validation_alias="startedAt", serialization_alias="startedAt", default=None)
    status: Literal["PARTIAL", "FINAL"] | None = Field(
        default=None, description="Completeness status for resource usage reporting."
    )
    usage_summary: ResourceUsageSummary | None = Field(
        validation_alias="usageSummary", serialization_alias="usageSummary", default=None
    )
