from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MethodProgressEntry(SimScaleModel):
    """A progress entry from the method engine."""

    checkpoint: Any | None = Field(default=None)
    percentage: Any | None = Field(default=None)
