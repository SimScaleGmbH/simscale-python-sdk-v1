from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.log_entry import LogEntry


class EventLogResponse(SimScaleModel):
    entries: list[LogEntry]
