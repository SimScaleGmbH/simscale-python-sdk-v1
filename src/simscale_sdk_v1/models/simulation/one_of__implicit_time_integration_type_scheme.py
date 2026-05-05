from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.hht_time_integration_scheme import HhtTimeIntegrationScheme
from simscale_sdk_v1.models.simulation.newmark_time_integration_scheme import NewmarkTimeIntegrationScheme

_ONE_OF__IMPLICIT_TIME_INTEGRATION_TYPE_SCHEME_VARIANTS: dict[str, type] = {
    "HHT": HhtTimeIntegrationScheme,
    "NEWMARK": NewmarkTimeIntegrationScheme,
}

OneOf_ImplicitTimeIntegrationTypeScheme = Annotated[
    Union[HhtTimeIntegrationScheme, NewmarkTimeIntegrationScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__IMPLICIT_TIME_INTEGRATION_TYPE_SCHEME_VARIANTS,
        )
    ),
]
