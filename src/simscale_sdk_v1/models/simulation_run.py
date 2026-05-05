from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation_run_compute_resource import SimulationRunComputeResource
from simscale_sdk_v1.models.status import Status


class SimulationRun(SimScaleModel):
    run_id: str | None = Field(validation_alias="runId", serialization_alias="runId", default=None)
    name: str = Field(description="The name of the simulation run.")
    created_at: datetime | None = Field(
        validation_alias="createdAt",
        serialization_alias="createdAt",
        default=None,
        description="The time when the simulation run was created.",
    )
    started_at: datetime | None = Field(
        validation_alias="startedAt",
        serialization_alias="startedAt",
        default=None,
        description="The time when the simulation run was started.",
    )
    finished_at: datetime | None = Field(
        validation_alias="finishedAt",
        serialization_alias="finishedAt",
        default=None,
        description="The time when the simulation run was finished.",
    )
    duration: str | None = Field(default=None, description="The actual duration of the simulation run.")
    compute_resource: SimulationRunComputeResource | None = Field(
        validation_alias="computeResource", serialization_alias="computeResource", default=None
    )
    status: Status | None = Field(default=None)
    progress: float | None = Field(
        default=None, description="The current progress while the simulation run is in progress."
    )
