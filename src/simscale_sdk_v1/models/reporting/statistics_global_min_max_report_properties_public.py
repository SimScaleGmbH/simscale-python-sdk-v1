from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.step_selector import StepSelector


class StatisticsGlobalMinMaxReportPropertiesPublic(SimScaleModel):
    """The global min/max report configuration as returned in a report response: the scalar field whose extremes were sought and the solution steps that were scanned."""

    report_type: str = Field(
        validation_alias="reportType", serialization_alias="reportType", default="STATISTICS_GLOBAL_MIN_MAX"
    )
    scalar_field: ScalarField = Field(validation_alias="scalarField", serialization_alias="scalarField")
    steps: StepSelector
