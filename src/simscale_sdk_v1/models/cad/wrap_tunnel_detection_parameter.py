from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.length import Length


class WrapTunnelDetectionParameter(SimScaleModel):
    selected: Literal["wrap_surface_tunnel_detection_manual", "wrap_surface_tunnel_detection_auto"] = Field(
        description="Defines the method to detect tunnels in the input bodies. It can be either: - `wrap_surface_tunnel_detection_manual`, in which case `min_tunnel_diameter` must be specified, or - `wrap_surface_tunnel_detection_auto`, in which case the tunnel detection happens automatically."
    )
    min_tunnel_diameter: Length | None = Field(default=None)
