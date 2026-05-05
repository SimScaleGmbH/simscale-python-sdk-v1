from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.average_velocity_momentum_source import AverageVelocityMomentumSource
from simscale_sdk_v1.models.simulation.fan_pressure_drop_momentum_source import FanPressureDropMomentumSource
from simscale_sdk_v1.models.simulation.friction_velocity_momentum_source import FrictionVelocityMomentumSource

_ONE_OF__ADVANCED_CONCEPTS_MOMENTUM_SOURCES_VARIANTS: dict[str, type] = {
    "AVERAGE_VELOCITY": AverageVelocityMomentumSource,
    "FAN_PRESSURE_DROP": FanPressureDropMomentumSource,
    "FRICTION_VELOCITY_SOURCE": FrictionVelocityMomentumSource,
}

OneOf_AdvancedConceptsMomentumSources = Annotated[
    Union[AverageVelocityMomentumSource, FanPressureDropMomentumSource, FrictionVelocityMomentumSource],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_MOMENTUM_SOURCES_VARIANTS,
        )
    ),
]
