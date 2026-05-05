from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.derived_heat_flux import DerivedHeatFlux
from simscale_sdk_v1.models.simulation.fixed_heat_flux import FixedHeatFlux
from simscale_sdk_v1.models.simulation.fixed_power_heat_flux import FixedPowerHeatFlux

_ONE_OF__EXTERNAL_WALL_HEAT_FLUX_TBC_HEAT_FLUX_VARIANTS: dict[str, type] = {
    "DERIVED": DerivedHeatFlux,
    "FIXED": FixedHeatFlux,
    "FIXED_POWER": FixedPowerHeatFlux,
}

OneOf_ExternalWallHeatFluxTBCHeatFlux = Annotated[
    Union[DerivedHeatFlux, FixedHeatFlux, FixedPowerHeatFlux],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__EXTERNAL_WALL_HEAT_FLUX_TBC_HEAT_FLUX_VARIANTS,
        )
    ),
]
