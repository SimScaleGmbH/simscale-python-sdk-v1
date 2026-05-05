from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StatisticsCentroidMetric(SimScaleModel):
    """Centroid [x, y, z] coordinates paired with their length unit."""

    value: list[float] | None = Field(
        default=None, description="The [x, y, z] coordinates of the centroid in model space."
    )
    unit: str | None = Field(default=None, description="Length unit for the coordinates (e.g. 'm', 'in').")
