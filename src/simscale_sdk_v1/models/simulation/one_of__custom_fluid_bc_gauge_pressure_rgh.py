from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fan_pbc import FanPBC
from simscale_sdk_v1.models.simulation.fixed_flux_pbc import FixedFluxPBC
from simscale_sdk_v1.models.simulation.fixed_gradient_pbc import FixedGradientPBC
from simscale_sdk_v1.models.simulation.fixed_value_pbc import FixedValuePBC
from simscale_sdk_v1.models.simulation.freestream_pbc import FreestreamPBC
from simscale_sdk_v1.models.simulation.hydrostatic_fan_pbc import HydrostaticFanPBC
from simscale_sdk_v1.models.simulation.mean_value_pbc import MeanValuePBC
from simscale_sdk_v1.models.simulation.symmetry_pbc import SymmetryPBC
from simscale_sdk_v1.models.simulation.total_pbc import TotalPBC
from simscale_sdk_v1.models.simulation.zero_gradient_pbc import ZeroGradientPBC

# Please choose a boundary condition for modified gauge pressure (p_rgh). Learn more.
_ONE_OF__CUSTOM_FLUID_BC_GAUGE_PRESSURE_RGH_VARIANTS: dict[str, type] = {
    "SYMMETRY": SymmetryPBC,
    "FAN_PRESSURE": FanPBC,
    "FIXED_FLUX_PRESSURE": FixedFluxPBC,
    "FIXED_GRADIENT": FixedGradientPBC,
    "FIXED_VALUE": FixedValuePBC,
    "FREESTREAM": FreestreamPBC,
    "FIXED_MEAN": MeanValuePBC,
    "ZERO_GRADIENT": ZeroGradientPBC,
    "TOTAL_PRESSURE": TotalPBC,
    "HYDROSTATIC_ISOTHERMAL_FAN_PRESSURE": HydrostaticFanPBC,
}

OneOf_CustomFluidBCGaugePressureRgh = Annotated[
    Union[
        SymmetryPBC,
        FanPBC,
        FixedFluxPBC,
        FixedGradientPBC,
        FixedValuePBC,
        FreestreamPBC,
        MeanValuePBC,
        ZeroGradientPBC,
        TotalPBC,
        HydrostaticFanPBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_GAUGE_PRESSURE_RGH_VARIANTS,
        )
    ),
]
