from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.vector import Vector


class PointPair(SimScaleModel):
    """Hit line in meters to be used in the viewer."""

    point1: Vector
    point2: Vector
