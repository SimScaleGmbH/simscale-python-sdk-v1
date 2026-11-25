from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.vector import Vector


class Arrow(SimScaleModel):
    """Hint arrow to be used in the viewer: origin in meters, unit direction."""

    origin: Vector
    direction: Vector
