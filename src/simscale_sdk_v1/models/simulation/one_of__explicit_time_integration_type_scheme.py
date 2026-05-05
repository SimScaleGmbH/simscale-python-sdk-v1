from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.central_diff_time_integration_scheme import CentralDiffTimeIntegrationScheme
from simscale_sdk_v1.models.simulation.tchamwa_time_integration_scheme import TchamwaTimeIntegrationScheme

_ONE_OF__EXPLICIT_TIME_INTEGRATION_TYPE_SCHEME_VARIANTS: dict[str, type] = {
    "CENTRAL_DIFF": CentralDiffTimeIntegrationScheme,
    "TCHAMWA": TchamwaTimeIntegrationScheme,
}

OneOf_ExplicitTimeIntegrationTypeScheme = Annotated[
    Union[CentralDiffTimeIntegrationScheme, TchamwaTimeIntegrationScheme],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__EXPLICIT_TIME_INTEGRATION_TYPE_SCHEME_VARIANTS,
        )
    ),
]
