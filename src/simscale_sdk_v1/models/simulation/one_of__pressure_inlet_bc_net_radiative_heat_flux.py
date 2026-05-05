from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.greybody_diffusive_rsbc import GreybodyDiffusiveRSBC
from simscale_sdk_v1.models.simulation.open_window_rsbc import OpenWindowRSBC

_ONE_OF__PRESSURE_INLET_BC_NET_RADIATIVE_HEAT_FLUX_VARIANTS: dict[str, type] = {
    "GREYBODY_DIFFUSIVE": GreybodyDiffusiveRSBC,
    "OPEN_WINDOW": OpenWindowRSBC,
}

OneOf_PressureInletBCNetRadiativeHeatFlux = Annotated[
    Union[GreybodyDiffusiveRSBC, OpenWindowRSBC],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PRESSURE_INLET_BC_NET_RADIATIVE_HEAT_FLUX_VARIANTS,
        )
    ),
]
