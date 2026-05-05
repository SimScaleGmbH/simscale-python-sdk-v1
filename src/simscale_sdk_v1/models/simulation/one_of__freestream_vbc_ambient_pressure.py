from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_value_pbc import FixedValuePBC
from simscale_sdk_v1.models.simulation.hydrostatic_isothermal_freestream_pbc import HydrostaticIsothermalFreestreamPBC

_ONE_OF__FREESTREAM_VBC_AMBIENT_PRESSURE_VARIANTS: dict[str, type] = {
    "FIXED_VALUE": FixedValuePBC,
    "HYDROSTATIC_ISOTHERMAL_FREESTREAM_PRESSURE": HydrostaticIsothermalFreestreamPBC,
}

OneOf_FreestreamVBCAmbientPressure = Annotated[
    Union[FixedValuePBC, HydrostaticIsothermalFreestreamPBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FREESTREAM_VBC_AMBIENT_PRESSURE_VARIANTS,
        )
    ),
]
