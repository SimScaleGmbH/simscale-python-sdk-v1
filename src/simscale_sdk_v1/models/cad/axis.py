from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.vector import Vector


class Axis(SimScaleModel):
    """Axis of rotation."""

    value: Vector | None = Field(default=None)
