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

# This parameter determines the fineness of the mesh and affects the overall number of cells. It is recommended to start with the coarse setting. Find out more.Note: This setting will impact the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.
_ONE_OF__REGION_REFINEMENT_WIND_COMFORT_NEW_FINENESS_VARIANTS: dict[str, type] = {
    "VERY_COARSE": PacefishFinenessVeryCoarse,
    "COARSE": PacefishFinenessCoarse,
    "MODERATE": PacefishFinenessModerate,
    "FINE": PacefishFinenessFine,
    "VERY_FINE": PacefishFinenessVeryFine,
    "TARGET_SIZE": PacefishFinenessTargetSize,
}

OneOf_RegionRefinementWindComfortNewFineness = Annotated[
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
            variants=_ONE_OF__REGION_REFINEMENT_WIND_COMFORT_NEW_FINENESS_VARIANTS,
        )
    ),
]
