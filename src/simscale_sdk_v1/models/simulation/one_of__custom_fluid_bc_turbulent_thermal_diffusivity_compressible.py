from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.calculated_tdcbc import CalculatedTDCBC
from simscale_sdk_v1.models.simulation.fixed_gradient_tdcbc import FixedGradientTDCBC
from simscale_sdk_v1.models.simulation.fixed_value_tdcbc import FixedValueTDCBC
from simscale_sdk_v1.models.simulation.full_resolution_tdcbc import FullResolutionTDCBC
from simscale_sdk_v1.models.simulation.symmetry_tdcbc import SymmetryTDCBC
from simscale_sdk_v1.models.simulation.wall_function_tdcbc import WallFunctionTDCBC
from simscale_sdk_v1.models.simulation.zero_gradient_tdcbc import ZeroGradientTDCBC

# Dynamic turbulent thermal diffusivity (alpha_Sgs) represents the rate of turbulent heat transfer.
_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_THERMAL_DIFFUSIVITY_COMPRESSIBLE_VARIANTS: dict[str, type] = {
    "CALCULATED": CalculatedTDCBC,
    "FIXED_GRADIENT": FixedGradientTDCBC,
    "FIXED_VALUE": FixedValueTDCBC,
    "ZERO_GRADIENT": ZeroGradientTDCBC,
    "SYMMETRY": SymmetryTDCBC,
    "WALL_FUNCTION": WallFunctionTDCBC,
    "FULL_RESOLUTION": FullResolutionTDCBC,
}

OneOf_CustomFluidBCTurbulentThermalDiffusivityCompressible = Annotated[
    Union[
        CalculatedTDCBC,
        FixedGradientTDCBC,
        FixedValueTDCBC,
        ZeroGradientTDCBC,
        SymmetryTDCBC,
        WallFunctionTDCBC,
        FullResolutionTDCBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_THERMAL_DIFFUSIVITY_COMPRESSIBLE_VARIANTS,
        )
    ),
]
