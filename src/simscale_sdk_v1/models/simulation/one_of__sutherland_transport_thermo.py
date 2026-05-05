from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.e_const_thermo import EConstThermo
from simscale_sdk_v1.models.simulation.h_const_thermo import HConstThermo

_ONE_OF__SUTHERLAND_TRANSPORT_THERMO_VARIANTS: dict[str, type] = {
    "ECONST": EConstThermo,
    "HCONST": HConstThermo,
}

OneOf_SutherlandTransportThermo = Annotated[
    Union[EConstThermo, HConstThermo],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SUTHERLAND_TRANSPORT_THERMO_VARIANTS,
        )
    ),
]
