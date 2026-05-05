from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.wrap_tunnel_detection_parameter import WrapTunnelDetectionParameter


class WrapOccurrencesParameters(SimScaleModel):
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
    wrap_type: Literal["features", "outside"] = Field(
        description="Defines the behavior of the wrapper. It can be either: - `features`: to try preserve the edges of the selected volumes, or - `outside`: to create a body closely fitted to the selected volumes."
    )
    resolution: float = Field(
        description="Resolution of the wrapper, the higher the resolution, the closer the result would be to the selected volumes. This value is defined between 1 and 10."
    )
    allow_tunnels: bool = Field(
        description="Defines the behavior with respect to tunnels in the selected bodies. If `true`, the wrapper will attempt to go through the tunnels."
    )
    cap_tunnels: bool = Field(
        description="Defines the behavior with respect to tunnels in the selected bodies. If `true`, the wrapper will create patches to cover the tunnels."
    )
    tunnel_detection: WrapTunnelDetectionParameter
    replace_each: bool = Field(
        description="Controls the result. If `true`, each body will be replaced singularly; otherwise all bodies will be replaced by a single primitive."
    )
