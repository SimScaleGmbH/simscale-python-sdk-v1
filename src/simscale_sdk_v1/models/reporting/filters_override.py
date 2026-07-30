from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.displacement import Displacement


class FiltersOverride(SimScaleModel):
    """Partial filter settings applied as an override on top of the state's own filters. All properties are optional; only those provided are overridden."""

    displacement: Displacement | None = Field(default=None)
