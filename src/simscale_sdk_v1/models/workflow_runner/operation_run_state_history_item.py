from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OperationRunStateHistoryItem(SimScaleModel):
    """Item in the operation run state history. Each history item stores the new state that the operation run has entered at the stored timestamp."""

    change_timestamp: datetime | None = Field(
        validation_alias="changeTimestamp", serialization_alias="changeTimestamp", default=None
    )
    operation_run_state: (
        Literal[
            "CREATED",
            "SCHEDULED",
            "RUNNING",
            "TO_BE_REPROCESSED",
            "SUCCEEDED",
            "FAILED",
            "CANCELED",
            "PROCESSING",
            "PROCESSED",
            "UNPROCESSED",
        ]
        | None
    ) = Field(
        validation_alias="operationRunState",
        serialization_alias="operationRunState",
        default=None,
        description="Possible states of an operation run.",
    )
