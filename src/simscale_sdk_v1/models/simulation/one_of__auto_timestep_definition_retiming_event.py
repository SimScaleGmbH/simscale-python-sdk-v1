from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.collision_retiming_event import CollisionRetimingEvent
from simscale_sdk_v1.models.simulation.error_retiming_event import ErrorRetimingEvent
from simscale_sdk_v1.models.simulation.field_change_retiming_event import FieldChangeRetimingEvent
from simscale_sdk_v1.models.simulation.non_monotomous_residual_retiming_event import NonMonotomousResidualRetimingEvent

_ONE_OF__AUTO_TIMESTEP_DEFINITION_RETIMING_EVENT_VARIANTS: dict[str, type] = {
    "ERROR": ErrorRetimingEvent,
    "COLLISION": CollisionRetimingEvent,
    "FIELD_CHANGE": FieldChangeRetimingEvent,
    "NON_MONOTOMOUS_RESIDUAL": NonMonotomousResidualRetimingEvent,
}

OneOf_AutoTimestepDefinitionRetimingEvent = Annotated[
    Union[ErrorRetimingEvent, CollisionRetimingEvent, FieldChangeRetimingEvent, NonMonotomousResidualRetimingEvent],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__AUTO_TIMESTEP_DEFINITION_RETIMING_EVENT_VARIANTS,
        )
    ),
]
