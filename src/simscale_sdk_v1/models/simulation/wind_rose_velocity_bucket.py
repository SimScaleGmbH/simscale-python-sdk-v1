from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WindRoseVelocityBucket(SimScaleModel):
    from_: float | None = Field(validation_alias="from", serialization_alias="from", default=None)
    to: float | None = Field(default=None)
    fractions: list[float] | None = Field(default=None)
