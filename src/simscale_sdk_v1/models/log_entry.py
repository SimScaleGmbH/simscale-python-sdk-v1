from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_severity import LogSeverity


class LogEntry(SimScaleModel):
    severity: LogSeverity
    code: str = Field(description="Code for e.g. programmatic handling of error conditions.")
    message: str = Field(description="Human-readable description of the entry.")
    details: dict[str, Any] | None = Field(
        default=None, description="Additional data to interpret and handle the entry."
    )
