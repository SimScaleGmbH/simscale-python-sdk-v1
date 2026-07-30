from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StepSelector(SimScaleModel):
    """Selects which solution steps to scan. A step is one entry in the result sequence: a time-step for a transient analysis, or a frequency for a harmonic analysis. Set selection to FIRST or LAST for a single boundary step, ALL for every step, or INDICES for a specific set given in indices (0-based). indices applies only when selection is INDICES."""

    selection: Literal["FIRST", "LAST", "ALL", "INDICES"]
    indices: list[int] | None = Field(
        default=None, description="The 0-based step indices to scan; used only when selection is INDICES."
    )
