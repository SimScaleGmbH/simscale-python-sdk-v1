from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.cube_root_vol_les_delta import CubeRootVolLesDelta
from simscale_sdk_v1.models.simulation.smooth_les_delta import SmoothLesDelta

_ONE_OF__PRANDTL_LES_DELTA_DELTA_COEFFICIENT_VARIANTS: dict[str, type] = {
    "SMOOTH": SmoothLesDelta,
    "CUBE_ROOT_VOL": CubeRootVolLesDelta,
}

OneOf_PrandtlLesDeltaDeltaCoefficient = Annotated[
    Union[SmoothLesDelta, CubeRootVolLesDelta],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__PRANDTL_LES_DELTA_DELTA_COEFFICIENT_VARIANTS,
        )
    ),
]
