from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.wrap_tunnel_detection_parameter import WrapTunnelDetectionParameter


class WrapOccurrencesParameters(SimScaleModel):
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
    wrap_type: Literal["features", "outside"] = Field(
        description='Defines the behavior of the wrapper. It can be either: - `features` (shown in the UI as "Snap to edges"): to try to preserve the edges of the selected volumes, or - `outside` (shown in the UI as "Fit to surface"): to create a body closely fitted to the selected volumes.'
    )
    resolution: float = Field(
        description="Resolution of the wrapper, the higher the resolution, the closer the result would be to the selected volumes. Must be a whole number between 1 and 10."
    )
    allow_tunnels: bool = Field(
        description="Defines the behavior with respect to tunnels in the selected bodies. If `true`, the wrapper will attempt to go through the tunnels."
    )
    cap_tunnels: bool = Field(
        description="Defines the behavior with respect to tunnels in the selected bodies. If `true`, the wrapper will create patches to cover the tunnels."
    )
    tunnel_detection: WrapTunnelDetectionParameter
    replace_each: bool = Field(
        description="Controls the result. If `true`, each body is wrapped individually; otherwise, one wrap body encloses all selected bodies."
    )
