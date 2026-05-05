from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.pacefish_fineness_coarse import PacefishFinenessCoarse
from simscale_sdk_v1.models.simulation.pacefish_fineness_fine import PacefishFinenessFine
from simscale_sdk_v1.models.simulation.pacefish_fineness_moderate import PacefishFinenessModerate
from simscale_sdk_v1.models.simulation.pacefish_fineness_target_size import PacefishFinenessTargetSize
from simscale_sdk_v1.models.simulation.pacefish_fineness_very_coarse import PacefishFinenessVeryCoarse
from simscale_sdk_v1.models.simulation.pacefish_fineness_very_fine import PacefishFinenessVeryFine

_ONE_OF__WIND_COMFORT_MESH_WIND_COMFORT_FINENESS_VARIANTS: dict[str, type] = {
    "VERY_COARSE": PacefishFinenessVeryCoarse,
    "COARSE": PacefishFinenessCoarse,
    "MODERATE": PacefishFinenessModerate,
    "FINE": PacefishFinenessFine,
    "VERY_FINE": PacefishFinenessVeryFine,
    "TARGET_SIZE": PacefishFinenessTargetSize,
}

OneOf_WindComfortMeshWindComfortFineness = Annotated[
    Union[
        PacefishFinenessVeryCoarse,
        PacefishFinenessCoarse,
        PacefishFinenessModerate,
        PacefishFinenessFine,
        PacefishFinenessVeryFine,
        PacefishFinenessTargetSize,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__WIND_COMFORT_MESH_WIND_COMFORT_FINENESS_VARIANTS,
        )
    ),
]
