from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.adiabatic_tbc import AdiabaticTBC
from simscale_sdk_v1.models.simulation.external_wall_heat_flux_tbc import ExternalWallHeatFluxTBC
from simscale_sdk_v1.models.simulation.fixed_gradient_tbc import FixedGradientTBC
from simscale_sdk_v1.models.simulation.fixed_value_tbc import FixedValueTBC
from simscale_sdk_v1.models.simulation.inlet_outlet_tbc import InletOutletTBC
from simscale_sdk_v1.models.simulation.symmetry_tbc import SymmetryTBC
from simscale_sdk_v1.models.simulation.total_tbc import TotalTBC
from simscale_sdk_v1.models.simulation.turbulent_heat_flux_tbc import TurbulentHeatFluxTBC
from simscale_sdk_v1.models.simulation.wall_heat_transfer_tbc import WallHeatTransferTBC

# Please choose a boundary condition for temperature (T).
_ONE_OF__CUSTOM_FLUID_BC_TEMPERATURE_VARIANTS: dict[str, type] = {
    "EXTERNAL_WALL_HEAT_FLUX_TEMPERATURE": ExternalWallHeatFluxTBC,
    "FIXED_GRADIENT": FixedGradientTBC,
    "FIXED_VALUE": FixedValueTBC,
    "INLET_OUTLET": InletOutletTBC,
    "ADIABATIC": AdiabaticTBC,
    "SYMMETRY": SymmetryTBC,
    "TOTAL_TEMPERATURE": TotalTBC,
    "TURBULENT_HEAT_FLUX_TEMPERATURE": TurbulentHeatFluxTBC,
    "WALL_HEAT_TRANSFER": WallHeatTransferTBC,
}

OneOf_CustomFluidBCTemperature = Annotated[
    Union[
        ExternalWallHeatFluxTBC,
        FixedGradientTBC,
        FixedValueTBC,
        InletOutletTBC,
        AdiabaticTBC,
        SymmetryTBC,
        TotalTBC,
        TurbulentHeatFluxTBC,
        WallHeatTransferTBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__CUSTOM_FLUID_BC_TEMPERATURE_VARIANTS,
        )
    ),
]
