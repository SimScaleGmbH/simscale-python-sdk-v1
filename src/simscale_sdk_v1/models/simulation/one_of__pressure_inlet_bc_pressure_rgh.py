from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.hydrostatic_isothermal_total_pbc import HydrostaticIsothermalTotalPBC
from simscale_sdk_v1.models.simulation.total_pbc import TotalPBC

_ONE_OF__PRESSURE_INLET_BC_PRESSURE_RGH_VARIANTS: dict[str, type] = {
    "TOTAL_PRESSURE": TotalPBC,
    "HYDROSTATIC_ISOTHERMAL_TOTAL_PRESSURE": HydrostaticIsothermalTotalPBC,
}

OneOf_PressureInletBCPressureRgh = Annotated[
    Union[TotalPBC, HydrostaticIsothermalTotalPBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PRESSURE_INLET_BC_PRESSURE_RGH_VARIANTS,
        )
    ),
]
