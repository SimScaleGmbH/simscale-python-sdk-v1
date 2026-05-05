from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.euler_time_differentiation_scheme import EulerTimeDifferentiationScheme
from simscale_sdk_v1.models.simulation.local_euler_time_differentiation_scheme import (
    LocalEulerTimeDifferentiationScheme,
)
from simscale_sdk_v1.models.simulation.steadystate_time_differentiation_scheme import (
    SteadystateTimeDifferentiationScheme,
)

# With this option, you can choose your desired time-differentiation scheme:For steady-state simulations, choose steadyState.Euler is a first-order implicit and bounded scheme. If unsure, try this scheme first.localEuler is a local time-step scheme, which is first-order implicit and bounded.
_ONE_OF__TIME_DIFFERENTIATION_SCHEMES_FOR_DEFAULT_VARIANTS: dict[str, type] = {
    "EULER": EulerTimeDifferentiationScheme,
    "LOCAL_EULER": LocalEulerTimeDifferentiationScheme,
    "STEADYSTATE": SteadystateTimeDifferentiationScheme,
}

OneOf_TimeDifferentiationSchemesForDefault = Annotated[
    Union[EulerTimeDifferentiationScheme, LocalEulerTimeDifferentiationScheme, SteadystateTimeDifferentiationScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__TIME_DIFFERENTIATION_SCHEMES_FOR_DEFAULT_VARIANTS,
        )
    ),
]
