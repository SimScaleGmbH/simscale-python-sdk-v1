from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.stationary_time_dependency import StationaryTimeDependency
from simscale_sdk_v1.models.simulation.transient_time_dependency import TransientTimeDependency

# Steady-state: Steady-state simulations are time-independent, that is, the equations solved do not include time derivatives. If you are only interested in the converged solution, consider a steady-state simulation.Transient: Transient simulations account for time-dependent effects, that is, the associated flow variables vary with respect to time.
_ONE_OF__HEAT_TRANSFER_TIME_DEPENDENCY_VARIANTS: dict[str, type] = {
    "TRANSIENT": TransientTimeDependency,
    "STATIONARY": StationaryTimeDependency,
}

OneOf_HeatTransferTimeDependency = Annotated[
    Union[TransientTimeDependency, StationaryTimeDependency],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__HEAT_TRANSFER_TIME_DEPENDENCY_VARIANTS,
        )
    ),
]
