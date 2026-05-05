from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.surface_water_vapor_flux_humidity_bc import SurfaceWaterVaporFluxHumidityBC
from simscale_sdk_v1.models.simulation.water_vapor_flux_humidity_bc import WaterVaporFluxHumidityBC
from simscale_sdk_v1.models.simulation.zero_gradient_humidity_bc import ZeroGradientHumidityBC

_ONE_OF__WALL_BC_RELATIVE_HUMIDITY_VARIANTS: dict[str, type] = {
    "ZERO_GRADIENT": ZeroGradientHumidityBC,
    "WATER_VAPOR_FLUX": WaterVaporFluxHumidityBC,
    "SURFACE_WATER_VAPOR_FLUX": SurfaceWaterVaporFluxHumidityBC,
}

OneOf_WallBCRelativeHumidity = Annotated[
    Union[ZeroGradientHumidityBC, WaterVaporFluxHumidityBC, SurfaceWaterVaporFluxHumidityBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WALL_BC_RELATIVE_HUMIDITY_VARIANTS,
        )
    ),
]
