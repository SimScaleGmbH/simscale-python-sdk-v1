from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_entry import LogEntry
from simscale_sdk_v1.models.log_severity import LogSeverity


class CheckResponse(SimScaleModel):
    severity: LogSeverity
    entries: list[LogEntry]
