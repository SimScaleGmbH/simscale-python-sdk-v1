from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length


class WindTunnelSizeCustom(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="WIND_TUNNEL_SIZE_CUSTOM",
        description="Schema name: WindTunnelSizeCustom",
    )
    height_extension: Dimensional_Length | None = Field(
        validation_alias="heightExtension", serialization_alias="heightExtension", default=None
    )
    side_extension: Dimensional_Length | None = Field(
        validation_alias="sideExtension", serialization_alias="sideExtension", default=None
    )
    inflow_extension: Dimensional_Length | None = Field(
        validation_alias="inflowExtension", serialization_alias="inflowExtension", default=None
    )
    outflow_extension: Dimensional_Length | None = Field(
        validation_alias="outflowExtension", serialization_alias="outflowExtension", default=None
    )
