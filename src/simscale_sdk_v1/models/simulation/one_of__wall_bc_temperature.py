from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.adiabatic_tbc import AdiabaticTBC
from simscale_sdk_v1.models.simulation.convection_radiation_tbc import ConvectionRadiationTBC
from simscale_sdk_v1.models.simulation.convection_tbc import ConvectionTBC
from simscale_sdk_v1.models.simulation.external_wall_heat_flux_tbc import ExternalWallHeatFluxTBC
from simscale_sdk_v1.models.simulation.fixed_value_tbc import FixedValueTBC
from simscale_sdk_v1.models.simulation.radiation_tbc import RadiationTBC
from simscale_sdk_v1.models.simulation.total_tbc import TotalTBC
from simscale_sdk_v1.models.simulation.turbulent_heat_flux_tbc import TurbulentHeatFluxTBC

# Please choose a boundary condition for temperature (T).
_ONE_OF__WALL_BC_TEMPERATURE_VARIANTS: dict[str, type] = {
    "EXTERNAL_WALL_HEAT_FLUX_TEMPERATURE": ExternalWallHeatFluxTBC,
    "FIXED_VALUE": FixedValueTBC,
    "ADIABATIC": AdiabaticTBC,
    "TOTAL_TEMPERATURE": TotalTBC,
    "TURBULENT_HEAT_FLUX_TEMPERATURE": TurbulentHeatFluxTBC,
    "CONVECTIVE_HEAT_TRANSFER": ConvectionTBC,
    "RADIATIVE_HEAT_TRANSFER": RadiationTBC,
    "CONVECTIVE_RADIATIVE_HEAT_TRANSFER": ConvectionRadiationTBC,
}

OneOf_WallBCTemperature = Annotated[
    Union[
        ExternalWallHeatFluxTBC,
        FixedValueTBC,
        AdiabaticTBC,
        TotalTBC,
        TurbulentHeatFluxTBC,
        ConvectionTBC,
        RadiationTBC,
        ConvectionRadiationTBC,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WALL_BC_TEMPERATURE_VARIANTS,
        )
    ),
]
