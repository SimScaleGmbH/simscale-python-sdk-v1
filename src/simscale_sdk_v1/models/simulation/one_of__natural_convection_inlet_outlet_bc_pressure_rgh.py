from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.ambient_pbc import AmbientPBC
from simscale_sdk_v1.models.simulation.hydrostatic_isothermal_total_pbc import HydrostaticIsothermalTotalPBC

_ONE_OF__NATURAL_CONVECTION_INLET_OUTLET_BC_PRESSURE_RGH_VARIANTS: dict[str, type] = {
    "AMBIENT_PRESSURE": AmbientPBC,
    "HYDROSTATIC_ISOTHERMAL_TOTAL_PRESSURE": HydrostaticIsothermalTotalPBC,
}

OneOf_NaturalConvectionInletOutletBCPressureRgh = Annotated[
    Union[AmbientPBC, HydrostaticIsothermalTotalPBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__NATURAL_CONVECTION_INLET_OUTLET_BC_PRESSURE_RGH_VARIANTS,
        )
    ),
]
