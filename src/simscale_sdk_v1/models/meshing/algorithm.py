from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.meshing.hex_dominant_snappy import HexDominantSnappy
from simscale_sdk_v1.models.meshing.polygrid_meshing import PolygridMeshing
from simscale_sdk_v1.models.meshing.simmetrix_meshing_electromagnetics import SimmetrixMeshingElectromagnetics
from simscale_sdk_v1.models.meshing.simmetrix_meshing_fluid import SimmetrixMeshingFluid
from simscale_sdk_v1.models.meshing.simmetrix_meshing_solid import SimmetrixMeshingSolid

_ALGORITHM_VARIANTS: dict[str, type] = {
    "SIMMETRIX_MESHING_FLUID_V16": SimmetrixMeshingFluid,
    "SIMMETRIX_MESHING_SOLID": SimmetrixMeshingSolid,
    "SIMMETRIX_MESHING_ELECTROMAGNETICS": SimmetrixMeshingElectromagnetics,
    "HEX_DOMINANT_SNAPPY_V5": HexDominantSnappy,
    "POLYGRID_MESHING": PolygridMeshing,
}

Algorithm = Annotated[
    Union[
        SimmetrixMeshingFluid,
        SimmetrixMeshingSolid,
        SimmetrixMeshingElectromagnetics,
        HexDominantSnappy,
        PolygridMeshing,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ALGORITHM_VARIANTS,
        )
    ),
]
