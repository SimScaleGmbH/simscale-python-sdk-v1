from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.stationary_time_dependency import StationaryTimeDependency
from simscale_sdk_v1.models.simulation.transient_time_dependency import TransientTimeDependency

# Steady-state: Steady-state simulations are time-independent. That is, the magnetic and thermal field are constant during the simulation.Transient: Transient simulations account for time-dependent effects where the magnetic and thermal field can change with time (e.g. due to Ohmic heating or boundary conditions).
_ONE_OF__TIME_HARMONIC_MAGNETICS_TIME_DEPENDENCY_VARIANTS: dict[str, type] = {
    "TRANSIENT": TransientTimeDependency,
    "STATIONARY": StationaryTimeDependency,
}

OneOf_TimeHarmonicMagneticsTimeDependency = Annotated[
    Union[TransientTimeDependency, StationaryTimeDependency],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__TIME_HARMONIC_MAGNETICS_TIME_DEPENDENCY_VARIANTS,
        )
    ),
]
