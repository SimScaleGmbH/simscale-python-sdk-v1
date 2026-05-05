from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.calculated_evcbc import CalculatedEVCBC
from simscale_sdk_v1.models.simulation.fixed_gradient_evcbc import FixedGradientEVCBC
from simscale_sdk_v1.models.simulation.fixed_value_evcbc import FixedValueEVCBC
from simscale_sdk_v1.models.simulation.full_resolution_evcbc import FullResolutionEVCBC
from simscale_sdk_v1.models.simulation.inlet_outlet_evcbc import InletOutletEVCBC
from simscale_sdk_v1.models.simulation.symmetry_evcbc import SymmetryEVCBC
from simscale_sdk_v1.models.simulation.wall_function_evcbc import WallFunctionEVCBC
from simscale_sdk_v1.models.simulation.zero_gradient_evcbc import ZeroGradientEVCBC

# Dissipation rate (epsilon) represents the rate of dissipation of turbulent kinetic energy (k). Learn more.
_ONE_OF__CUSTOM_FLUID_BC_EDDY_VISCOSITY_COMPRESSIBLE_VARIANTS: dict[str, type] = {
    "CALCULATED": CalculatedEVCBC,
    "SYMMETRY": SymmetryEVCBC,
    "FIXED_GRADIENT": FixedGradientEVCBC,
    "FIXED_VALUE": FixedValueEVCBC,
    "INLET_OUTLET": InletOutletEVCBC,
    "ZERO_GRADIENT": ZeroGradientEVCBC,
    "WALL_FUNCTION": WallFunctionEVCBC,
    "FULL_RESOLUTION": FullResolutionEVCBC,
}

OneOf_CustomFluidBCEddyViscosityCompressible = Annotated[
    Union[
        CalculatedEVCBC,
        SymmetryEVCBC,
        FixedGradientEVCBC,
        FixedValueEVCBC,
        InletOutletEVCBC,
        ZeroGradientEVCBC,
        WallFunctionEVCBC,
        FullResolutionEVCBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_EDDY_VISCOSITY_COMPRESSIBLE_VARIANTS,
        )
    ),
]
