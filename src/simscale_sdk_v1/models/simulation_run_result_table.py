from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation_run_result_category import SimulationRunResultCategory
from simscale_sdk_v1.models.simulation_run_result_direction import SimulationRunResultDirection
from simscale_sdk_v1.models.simulation_run_result_name import SimulationRunResultName


class SimulationRunResultTable(SimScaleModel):
    type_: str = Field(validation_alias="type", serialization_alias="type", default="TABLE")
    result_id: str | None = Field(
        validation_alias="resultId", serialization_alias="resultId", default=None, description="The result ID"
    )
    category: SimulationRunResultCategory | None = Field(default=None)
    direction: SimulationRunResultDirection | None = Field(default=None)
    name: SimulationRunResultName | None = Field(default=None)
    modified_at: datetime | None = Field(
        validation_alias="modifiedAt",
        serialization_alias="modifiedAt",
        default=None,
        description="The time when the result was last modified.",
    )
    workbench_url: str | None = Field(
        validation_alias="workbenchUrl",
        serialization_alias="workbenchUrl",
        default=None,
        description="URL for opening the table in the Workbench.",
    )
    available_export_formats: list[str] | None = Field(
        validation_alias="availableExportFormats",
        serialization_alias="availableExportFormats",
        default=None,
        description="Supported export format for this result.",
    )
