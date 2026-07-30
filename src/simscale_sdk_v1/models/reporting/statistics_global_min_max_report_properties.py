from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.step_selector import StepSelector


class StatisticsGlobalMinMaxReportProperties(SimScaleModel):
    """Configuration for a global min/max report: find the smallest and largest value of one scalar field across the entire model, over the selected steps, reporting each extreme's value, coordinates, part, and the step it occurred at."""

    report_type: str = Field(
        validation_alias="reportType", serialization_alias="reportType", default="STATISTICS_GLOBAL_MIN_MAX"
    )
    scalar_field: ScalarField = Field(validation_alias="scalarField", serialization_alias="scalarField")
    steps: StepSelector
    topology_label_by_name: dict[str, str] | None = Field(
        validation_alias="topologyLabelByName",
        serialization_alias="topologyLabelByName",
        default=None,
        description="Mesh-part-name to user-facing label mapping, used to report the extreme's part by label rather than internal mesh name.",
    )
