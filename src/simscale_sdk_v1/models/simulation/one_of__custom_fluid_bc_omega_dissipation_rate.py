from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_gradient_obc import FixedGradientOBC
from simscale_sdk_v1.models.simulation.fixed_value_obc import FixedValueOBC
from simscale_sdk_v1.models.simulation.full_resolution_obc import FullResolutionOBC
from simscale_sdk_v1.models.simulation.inlet_outlet_obc import InletOutletOBC
from simscale_sdk_v1.models.simulation.symmetry_obc import SymmetryOBC
from simscale_sdk_v1.models.simulation.wall_function_obc import WallFunctionOBC
from simscale_sdk_v1.models.simulation.zero_gradient_obc import ZeroGradientOBC

# Specific dissipation rate (omega) represents the specific rate of dissipation of turbulent kinetic energy (k). Learn more.
_ONE_OF__CUSTOM_FLUID_BC_OMEGA_DISSIPATION_RATE_VARIANTS: dict[str, type] = {
    "SYMMETRY": SymmetryOBC,
    "FIXED_GRADIENT": FixedGradientOBC,
    "FIXED_VALUE": FixedValueOBC,
    "INLET_OUTLET": InletOutletOBC,
    "ZERO_GRADIENT": ZeroGradientOBC,
    "WALL_FUNCTION": WallFunctionOBC,
    "FULL_RESOLUTION": FullResolutionOBC,
}

OneOf_CustomFluidBCOmegaDissipationRate = Annotated[
    Union[
        SymmetryOBC,
        FixedGradientOBC,
        FixedValueOBC,
        InletOutletOBC,
        ZeroGradientOBC,
        WallFunctionOBC,
        FullResolutionOBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_OMEGA_DISSIPATION_RATE_VARIANTS,
        )
    ),
]
