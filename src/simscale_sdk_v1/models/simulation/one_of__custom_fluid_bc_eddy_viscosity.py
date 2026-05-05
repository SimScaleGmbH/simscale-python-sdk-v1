from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.calculated_evbc import CalculatedEVBC
from simscale_sdk_v1.models.simulation.fixed_gradient_evbc import FixedGradientEVBC
from simscale_sdk_v1.models.simulation.fixed_value_evbc import FixedValueEVBC
from simscale_sdk_v1.models.simulation.full_resolution_evbc import FullResolutionEVBC
from simscale_sdk_v1.models.simulation.inlet_outlet_evbc import InletOutletEVBC
from simscale_sdk_v1.models.simulation.symmetry_evbc import SymmetryEVBC
from simscale_sdk_v1.models.simulation.wall_function_evbc import WallFunctionEVBC
from simscale_sdk_v1.models.simulation.zero_gradient_evbc import ZeroGradientEVBC

# Dynamic eddy viscosity (muSgs) is a sub-grid scale viscosity used to model the unresolved turbulent eddies in Large Eddy Simulations. Choose a boundary type.
_ONE_OF__CUSTOM_FLUID_BC_EDDY_VISCOSITY_VARIANTS: dict[str, type] = {
    "CALCULATED": CalculatedEVBC,
    "SYMMETRY": SymmetryEVBC,
    "FIXED_GRADIENT": FixedGradientEVBC,
    "FIXED_VALUE": FixedValueEVBC,
    "INLET_OUTLET": InletOutletEVBC,
    "ZERO_GRADIENT": ZeroGradientEVBC,
    "WALL_FUNCTION": WallFunctionEVBC,
    "FULL_RESOLUTION": FullResolutionEVBC,
}

OneOf_CustomFluidBCEddyViscosity = Annotated[
    Union[
        CalculatedEVBC,
        SymmetryEVBC,
        FixedGradientEVBC,
        FixedValueEVBC,
        InletOutletEVBC,
        ZeroGradientEVBC,
        WallFunctionEVBC,
        FullResolutionEVBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_EDDY_VISCOSITY_VARIANTS,
        )
    ),
]
