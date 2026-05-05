from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class WindTunnelSizeModerate(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WIND_TUNNEL_SIZE_MODERATE",
        description="Schema name: WindTunnelSizeModerate",
    )
