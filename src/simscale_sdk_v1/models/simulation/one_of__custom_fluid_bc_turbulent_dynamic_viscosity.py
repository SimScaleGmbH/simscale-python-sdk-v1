from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.calculated_dvbc import CalculatedDVBC
from simscale_sdk_v1.models.simulation.fixed_gradient_dvbc import FixedGradientDVBC
from simscale_sdk_v1.models.simulation.fixed_value_dvbc import FixedValueDVBC
from simscale_sdk_v1.models.simulation.full_resolution_dvbc import FullResolutionDVBC
from simscale_sdk_v1.models.simulation.inlet_outlet_dvbc import InletOutletDVBC
from simscale_sdk_v1.models.simulation.symmetry_dvbc import SymmetryDVBC
from simscale_sdk_v1.models.simulation.wall_function_dvbc import WallFunctionDVBC
from simscale_sdk_v1.models.simulation.zero_gradient_dvbc import ZeroGradientDVBC

# Turbulent dynamic viscosity is a model viscosity. It is required to account for the transport and dissipation effects lost in averaging the turbulence. Choose a boundary type.
_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_DYNAMIC_VISCOSITY_VARIANTS: dict[str, type] = {
    "CALCULATED": CalculatedDVBC,
    "FIXED_GRADIENT": FixedGradientDVBC,
    "FIXED_VALUE": FixedValueDVBC,
    "INLET_OUTLET": InletOutletDVBC,
    "ZERO_GRADIENT": ZeroGradientDVBC,
    "SYMMETRY": SymmetryDVBC,
    "WALL_FUNCTION": WallFunctionDVBC,
    "FULL_RESOLUTION": FullResolutionDVBC,
}

OneOf_CustomFluidBCTurbulentDynamicViscosity = Annotated[
    Union[
        CalculatedDVBC,
        FixedGradientDVBC,
        FixedValueDVBC,
        InletOutletDVBC,
        ZeroGradientDVBC,
        SymmetryDVBC,
        WallFunctionDVBC,
        FullResolutionDVBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_DYNAMIC_VISCOSITY_VARIANTS,
        )
    ),
]
