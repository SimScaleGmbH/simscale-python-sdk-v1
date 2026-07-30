from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.measured_scalar import MeasuredScalar
from simscale_sdk_v1.models.reporting.measured_vector import MeasuredVector


class GlobalMinMaxExtreme(SimScaleModel):
    """A single located extreme (the minimum or the maximum) with its value, coordinates, part, and step. Whether the value is node- or cell-based is given by the result's dataType."""

    value: MeasuredScalar | None = Field(default=None)
    coordinates: MeasuredVector | None = Field(default=None)
    part_name: str | None = Field(
        validation_alias="partName",
        serialization_alias="partName",
        default=None,
        description="The mesh part name the extreme was found on; null if the part could not be resolved.",
    )
    part_label: str | None = Field(
        validation_alias="partLabel",
        serialization_alias="partLabel",
        default=None,
        description="The user-facing label of that part (resolved from the mesh topology); null when no label is available or the part could not be resolved.",
    )
    step: Any | None = Field(
        default=None,
        description="The step at which this extreme occurred (a time-step for transient analyses, a frequency for harmonic, etc).",
    )
