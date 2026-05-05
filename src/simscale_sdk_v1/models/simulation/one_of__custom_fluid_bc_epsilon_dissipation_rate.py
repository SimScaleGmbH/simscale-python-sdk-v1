from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_gradient_ebc import FixedGradientEBC
from simscale_sdk_v1.models.simulation.fixed_value_ebc import FixedValueEBC
from simscale_sdk_v1.models.simulation.full_resolution_ebc import FullResolutionEBC
from simscale_sdk_v1.models.simulation.inlet_outlet_ebc import InletOutletEBC
from simscale_sdk_v1.models.simulation.mixing_length_inlet_ebc import MixingLengthInletEBC
from simscale_sdk_v1.models.simulation.symmetry_ebc import SymmetryEBC
from simscale_sdk_v1.models.simulation.wall_function_ebc import WallFunctionEBC
from simscale_sdk_v1.models.simulation.zero_gradient_ebc import ZeroGradientEBC

# Dissipation rate (epsilon) represents the rate of dissipation of turbulent kinetic energy (k). Learn more.
_ONE_OF__CUSTOM_FLUID_BC_EPSILON_DISSIPATION_RATE_VARIANTS: dict[str, type] = {
    "SYMMETRY": SymmetryEBC,
    "FIXED_GRADIENT": FixedGradientEBC,
    "FIXED_VALUE": FixedValueEBC,
    "INLET_OUTLET": InletOutletEBC,
    "TURBULENCE_MIXING_LENGTH_DISSIPATION_RATE_INLET": MixingLengthInletEBC,
    "ZERO_GRADIENT": ZeroGradientEBC,
    "WALL_FUNCTION": WallFunctionEBC,
    "FULL_RESOLUTION": FullResolutionEBC,
}

OneOf_CustomFluidBCEpsilonDissipationRate = Annotated[
    Union[
        SymmetryEBC,
        FixedGradientEBC,
        FixedValueEBC,
        InletOutletEBC,
        MixingLengthInletEBC,
        ZeroGradientEBC,
        WallFunctionEBC,
        FullResolutionEBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_EPSILON_DISSIPATION_RATE_VARIANTS,
        )
    ),
]
