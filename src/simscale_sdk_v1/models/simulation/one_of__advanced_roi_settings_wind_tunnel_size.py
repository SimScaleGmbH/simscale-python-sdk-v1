from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.wind_tunnel_size_custom import WindTunnelSizeCustom
from simscale_sdk_v1.models.simulation.wind_tunnel_size_large import WindTunnelSizeLarge
from simscale_sdk_v1.models.simulation.wind_tunnel_size_moderate import WindTunnelSizeModerate

_ONE_OF__ADVANCED_ROI_SETTINGS_WIND_TUNNEL_SIZE_VARIANTS: dict[str, type] = {
    "WIND_TUNNEL_SIZE_MODERATE": WindTunnelSizeModerate,
    "WIND_TUNNEL_SIZE_LARGE": WindTunnelSizeLarge,
    "WIND_TUNNEL_SIZE_CUSTOM": WindTunnelSizeCustom,
}

OneOf_AdvancedROISettingsWindTunnelSize = Annotated[
    Union[WindTunnelSizeModerate, WindTunnelSizeLarge, WindTunnelSizeCustom],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_ROI_SETTINGS_WIND_TUNNEL_SIZE_VARIANTS,
        )
    ),
]
