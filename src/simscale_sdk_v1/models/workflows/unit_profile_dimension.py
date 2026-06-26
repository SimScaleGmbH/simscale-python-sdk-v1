from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class UnitProfileDimension(SimScaleModel):
    """A profile of measurement units used for a particular dimension, containing a default unit and optionally additional units."""

    additional: list[str] | None = Field(default=None)
    default: str | None = Field(default=None)
