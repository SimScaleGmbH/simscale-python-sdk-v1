from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_acceleration import AutomaticAcceleration
from simscale_sdk_v1.models.simulation.full_rank_acceleration import FullRankAcceleration
from simscale_sdk_v1.models.simulation.low_rank_acceleration import LowRankAcceleration

_ONE_OF__ADVANCED_MUMPS_SETTINGS_MUMPS_ACCELERATION_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticAcceleration,
    "FULL_RANK": FullRankAcceleration,
    "LOW_RANK": LowRankAcceleration,
}

OneOf_AdvancedMUMPSSettingsMumpsAcceleration = Annotated[
    Union[AutomaticAcceleration, FullRankAcceleration, LowRankAcceleration],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_MUMPS_SETTINGS_MUMPS_ACCELERATION_VARIANTS,
        )
    ),
]
