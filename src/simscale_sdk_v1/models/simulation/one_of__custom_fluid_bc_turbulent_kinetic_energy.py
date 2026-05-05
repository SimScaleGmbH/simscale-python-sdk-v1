from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.fixed_gradient_tkebc import FixedGradientTKEBC
from simscale_sdk_v1.models.simulation.fixed_value_tkebc import FixedValueTKEBC
from simscale_sdk_v1.models.simulation.full_resolution_tkebc import FullResolutionTKEBC
from simscale_sdk_v1.models.simulation.inlet_outlet_tkebc import InletOutletTKEBC
from simscale_sdk_v1.models.simulation.intensity_kinetic_energy_inlet_tkebc import IntensityKineticEnergyInletTKEBC
from simscale_sdk_v1.models.simulation.symmetry_tkebc import SymmetryTKEBC
from simscale_sdk_v1.models.simulation.wall_function_tkebc import WallFunctionTKEBC
from simscale_sdk_v1.models.simulation.zero_gradient_tkebc import ZeroGradientTKEBC

# Please choose a boundary condition for turbulent kinetic energy (k).
_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_KINETIC_ENERGY_VARIANTS: dict[str, type] = {
    "SYMMETRY": SymmetryTKEBC,
    "FIXED_GRADIENT": FixedGradientTKEBC,
    "FIXED_VALUE": FixedValueTKEBC,
    "INLET_OUTLET": InletOutletTKEBC,
    "ZERO_GRADIENT": ZeroGradientTKEBC,
    "TURBULENT_INTENSITY_KINETIC_ENERGY_INLET": IntensityKineticEnergyInletTKEBC,
    "WALL_FUNCTION": WallFunctionTKEBC,
    "FULL_RESOLUTION": FullResolutionTKEBC,
}

OneOf_CustomFluidBCTurbulentKineticEnergy = Annotated[
    Union[
        SymmetryTKEBC,
        FixedGradientTKEBC,
        FixedValueTKEBC,
        InletOutletTKEBC,
        ZeroGradientTKEBC,
        IntensityKineticEnergyInletTKEBC,
        WallFunctionTKEBC,
        FullResolutionTKEBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_TURBULENT_KINETIC_ENERGY_VARIANTS,
        )
    ),
]
