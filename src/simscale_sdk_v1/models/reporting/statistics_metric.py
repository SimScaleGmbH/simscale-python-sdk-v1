from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StatisticsMetric(SimScaleModel):
    """A scalar metric value paired with its unit string."""

    value: float | None = Field(
        default=None, description="The numeric value, or null when the value could not be computed."
    )
    unit: str | None = Field(
        default=None,
        description="Unit string for this metric (e.g. 'm/s', 'Pa', 'Pa·m²'). Integral metrics carry a composite unit (fieldUnit × surfaceAreaUnit or fieldUnit × volumeUnit); all other metrics carry the plain scalar field unit.",
    )
