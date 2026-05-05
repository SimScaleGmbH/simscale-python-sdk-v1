from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__advanced_roi_settings_wind_tunnel_size import (
    OneOf_AdvancedROISettingsWindTunnelSize,
)


class AdvancedROISettings(SimScaleModel):
    wind_tunnel_size: OneOf_AdvancedROISettingsWindTunnelSize | None = Field(
        validation_alias="windTunnelSize", serialization_alias="windTunnelSize", default=None
    )
