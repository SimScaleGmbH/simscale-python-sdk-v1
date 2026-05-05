from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.const_transport import ConstTransport
from simscale_sdk_v1.models.simulation.herschel_bulkley_transport import HerschelBulkleyTransport
from simscale_sdk_v1.models.simulation.sutherland_transport import SutherlandTransport

_ONE_OF__FLUID_COMPRESSIBLE_MATERIAL_TRANSPORT_VARIANTS: dict[str, type] = {
    "CONST": ConstTransport,
    "SUTHERLAND": SutherlandTransport,
    "HERSCHEL_BULKLEY": HerschelBulkleyTransport,
}

OneOf_FluidCompressibleMaterialTransport = Annotated[
    Union[ConstTransport, SutherlandTransport, HerschelBulkleyTransport],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FLUID_COMPRESSIBLE_MATERIAL_TRANSPORT_VARIANTS,
        )
    ),
]
