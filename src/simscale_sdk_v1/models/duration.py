from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Duration(SimScaleModel):
    """An interval with the estimated duration for a simulation run or a mesh operation."""

    value: str | None = Field(default=None)
    interval_min: str | None = Field(validation_alias="intervalMin", serialization_alias="intervalMin", default=None)
    interval_max: str | None = Field(validation_alias="intervalMax", serialization_alias="intervalMax", default=None)
