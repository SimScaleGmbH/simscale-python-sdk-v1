from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_gradient_nbc import FixedGradientNBC
from simscale_sdk_v1.models.simulation.fixed_value_nbc import FixedValueNBC
from simscale_sdk_v1.models.simulation.full_resolution_nbc import FullResolutionNBC
from simscale_sdk_v1.models.simulation.inlet_outlet_nbc import InletOutletNBC
from simscale_sdk_v1.models.simulation.symmetry_nbc import SymmetryNBC
from simscale_sdk_v1.models.simulation.wall_function_nbc import WallFunctionNBC
from simscale_sdk_v1.models.simulation.zero_gradient_nbc import ZeroGradientNBC

# nuTilda is a Spalart-Allmaras variable which is a function of eddy viscosity. Choose a boundary type.
_ONE_OF__CUSTOM_FLUID_BC_NU_TILDA_VARIANTS: dict[str, type] = {
    "SYMMETRY": SymmetryNBC,
    "FIXED_GRADIENT": FixedGradientNBC,
    "FIXED_VALUE": FixedValueNBC,
    "INLET_OUTLET": InletOutletNBC,
    "ZERO_GRADIENT": ZeroGradientNBC,
    "WALL_FUNCTION": WallFunctionNBC,
    "FULL_RESOLUTION": FullResolutionNBC,
}

OneOf_CustomFluidBCNuTilda = Annotated[
    Union[
        SymmetryNBC,
        FixedGradientNBC,
        FixedValueNBC,
        InletOutletNBC,
        ZeroGradientNBC,
        WallFunctionNBC,
        FullResolutionNBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_NU_TILDA_VARIANTS,
        )
    ),
]
