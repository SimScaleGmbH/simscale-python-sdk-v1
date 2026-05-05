from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel


class Vector3D(SimScaleModel):
    x: float
    y: float
    z: float
