from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.field_change_target_calculation_type import FieldChangeTargetCalculationType
from simscale_sdk_v1.models.simulation.mixed_timestep_calculation_type import MixedTimestepCalculationType

_ONE_OF__FIELD_CHANGE_RETIMING_EVENT_TIMESTEP_CALCULATION_TYPE_VARIANTS: dict[str, type] = {
    "MIXED": MixedTimestepCalculationType,
    "FIELD_CHANGE_TARGET": FieldChangeTargetCalculationType,
}

OneOf_FieldChangeRetimingEventTimestepCalculationType = Annotated[
    Union[MixedTimestepCalculationType, FieldChangeTargetCalculationType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__FIELD_CHANGE_RETIMING_EVENT_TIMESTEP_CALCULATION_TYPE_VARIANTS,
        )
    ),
]
