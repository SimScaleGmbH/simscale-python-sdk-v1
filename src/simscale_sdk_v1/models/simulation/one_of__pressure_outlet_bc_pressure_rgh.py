from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_value_pbc import FixedValuePBC
from simscale_sdk_v1.models.simulation.hydrostatic_isothermal_pbc import HydrostaticIsothermalPBC
from simscale_sdk_v1.models.simulation.mean_value_pbc import MeanValuePBC

_ONE_OF__PRESSURE_OUTLET_BC_PRESSURE_RGH_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValuePBC,
    "FIXED_MEAN": MeanValuePBC,
    "HYDROSTATIC_ISOTHERMAL_PRESSURE": HydrostaticIsothermalPBC,
}

OneOf_PressureOutletBCPressureRgh = Annotated[
    Union[FixedValuePBC, MeanValuePBC, HydrostaticIsothermalPBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PRESSURE_OUTLET_BC_PRESSURE_RGH_VARIANTS,
        )
    ),
]
