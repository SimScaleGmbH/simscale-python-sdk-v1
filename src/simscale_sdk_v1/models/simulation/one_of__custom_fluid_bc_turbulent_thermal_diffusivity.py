from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.calculated_tdbc import CalculatedTDBC
from simscale_sdk_v1.models.simulation.fixed_gradient_tdbc import FixedGradientTDBC
from simscale_sdk_v1.models.simulation.fixed_value_tdbc import FixedValueTDBC
from simscale_sdk_v1.models.simulation.full_resolution_tdbc import FullResolutionTDBC
from simscale_sdk_v1.models.simulation.symmetry_tdbc import SymmetryTDBC
from simscale_sdk_v1.models.simulation.wall_function_tdbc import WallFunctionTDBC
from simscale_sdk_v1.models.simulation.zero_gradient_tdbc import ZeroGradientTDBC

# Dynamic turbulent thermal diffusivity (alpha_t) represents the rate of turbulent heat transfer.
_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_THERMAL_DIFFUSIVITY_VARIANTS: dict[str, type] = {
    "CALCULATED": CalculatedTDBC,
    "FIXED_GRADIENT": FixedGradientTDBC,
    "FIXED_VALUE": FixedValueTDBC,
    "ZERO_GRADIENT": ZeroGradientTDBC,
    "SYMMETRY": SymmetryTDBC,
    "WALL_FUNCTION": WallFunctionTDBC,
    "FULL_RESOLUTION": FullResolutionTDBC,
}

OneOf_CustomFluidBCTurbulentThermalDiffusivity = Annotated[
    Union[
        CalculatedTDBC,
        FixedGradientTDBC,
        FixedValueTDBC,
        ZeroGradientTDBC,
        SymmetryTDBC,
        WallFunctionTDBC,
        FullResolutionTDBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_THERMAL_DIFFUSIVITY_VARIANTS,
        )
    ),
]
