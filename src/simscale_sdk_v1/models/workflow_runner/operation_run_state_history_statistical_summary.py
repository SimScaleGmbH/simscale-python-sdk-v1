from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OperationRunStateHistoryStatisticalSummary(SimScaleModel):
    """Statistical summary information about the workflow run state history."""

    total_duration: int | None = Field(
        validation_alias="totalDuration", serialization_alias="totalDuration", default=None
    )
