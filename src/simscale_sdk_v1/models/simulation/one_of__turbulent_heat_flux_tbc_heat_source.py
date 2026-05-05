from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.flux_heat_source import FluxHeatSource
from simscale_sdk_v1.models.simulation.power_heat_source import PowerHeatSource

_ONE_OF__TURBULENT_HEAT_FLUX_TBC_HEAT_SOURCE_VARIANTS: dict[str, type] = {
    "FLUX": FluxHeatSource,
    "POWER": PowerHeatSource,
}

OneOf_TurbulentHeatFluxTBCHeatSource = Annotated[
    Union[FluxHeatSource, PowerHeatSource],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__TURBULENT_HEAT_FLUX_TBC_HEAT_SOURCE_VARIANTS,
        )
    ),
]
