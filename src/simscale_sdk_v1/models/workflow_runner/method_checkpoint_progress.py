from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MethodCheckpointProgress(SimScaleModel):
    """Checkpoint progress information."""

    code: str | None = Field(default=None)
    details: dict[str, Any] | None = Field(default=None)
