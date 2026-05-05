from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fan_pbc import FanPBC
from simscale_sdk_v1.models.simulation.hydrostatic_fan_pbc import HydrostaticFanPBC

_ONE_OF__FAN_BC_PRESSURE_RGH_VARIANTS: dict[str, type] = {
    "FAN_PRESSURE": FanPBC,
    "HYDROSTATIC_ISOTHERMAL_FAN_PRESSURE": HydrostaticFanPBC,
}

OneOf_FanBCPressureRgh = Annotated[
    Union[FanPBC, HydrostaticFanPBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FAN_BC_PRESSURE_RGH_VARIANTS,
        )
    ),
]
