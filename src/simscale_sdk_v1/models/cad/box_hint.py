from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.vector import Vector


class BoxHint(SimScaleModel):
    """Hint box in meters to be used in the viewer."""

    min: Vector
    max: Vector
