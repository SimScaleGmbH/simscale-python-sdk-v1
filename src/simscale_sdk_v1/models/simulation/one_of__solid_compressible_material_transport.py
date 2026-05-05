from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.const_an_iso_transport import ConstAnIsoTransport
from simscale_sdk_v1.models.simulation.const_cross_plane_orthotropic_transport import (
    ConstCrossPlaneOrthotropicTransport,
)
from simscale_sdk_v1.models.simulation.const_iso_transport import ConstIsoTransport

_ONE_OF__SOLID_COMPRESSIBLE_MATERIAL_TRANSPORT_VARIANTS: dict[str, type] = {
    "CONST_ISO": ConstIsoTransport,
    "CONST_AN_ISO": ConstAnIsoTransport,
    "CONST_CROSS_PLANE_ORTHO": ConstCrossPlaneOrthotropicTransport,
}

OneOf_SolidCompressibleMaterialTransport = Annotated[
    Union[ConstIsoTransport, ConstAnIsoTransport, ConstCrossPlaneOrthotropicTransport],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_COMPRESSIBLE_MATERIAL_TRANSPORT_VARIANTS,
        )
    ),
]
