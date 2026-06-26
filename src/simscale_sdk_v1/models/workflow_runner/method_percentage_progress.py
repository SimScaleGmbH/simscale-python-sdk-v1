from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MethodPercentageProgress(SimScaleModel):
    """Percentage progress value."""

    value: int | None = Field(default=None)
