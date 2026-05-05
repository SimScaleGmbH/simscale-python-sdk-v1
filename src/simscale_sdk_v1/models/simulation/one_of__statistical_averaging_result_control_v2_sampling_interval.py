from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.coarse_resolution import CoarseResolution
from simscale_sdk_v1.models.simulation.custom_resolution import CustomResolution
from simscale_sdk_v1.models.simulation.high_resolution import HighResolution
from simscale_sdk_v1.models.simulation.moderate_resolution import ModerateResolution

_ONE_OF__STATISTICAL_AVERAGING_RESULT_CONTROL_V2_SAMPLING_INTERVAL_VARIANTS: dict[str, type] = {
    "HIGH_RESOLUTION": HighResolution,
    "MODERATE_RESOLUTION": ModerateResolution,
    "COARSE_RESOLUTION": CoarseResolution,
    "CUSTOM_RESOLUTION": CustomResolution,
}

OneOf_StatisticalAveragingResultControlV2SamplingInterval = Annotated[
    Union[HighResolution, ModerateResolution, CoarseResolution, CustomResolution],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__STATISTICAL_AVERAGING_RESULT_CONTROL_V2_SAMPLING_INTERVAL_VARIANTS,
        )
    ),
]
