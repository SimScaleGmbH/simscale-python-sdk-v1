from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.explicit_time_integration_type import ExplicitTimeIntegrationType
from simscale_sdk_v1.models.simulation.implicit_time_integration_type import ImplicitTimeIntegrationType

_ONE_OF__SOLID_NUMERICS_MECHANICAL_TIME_INTEGRATION_TYPE_VARIANTS: dict[str, type] = {
    "IMPLICIT": ImplicitTimeIntegrationType,
    "EXPLICIT": ExplicitTimeIntegrationType,
}

OneOf_SolidNumericsMechanicalTimeIntegrationType = Annotated[
    Union[ImplicitTimeIntegrationType, ExplicitTimeIntegrationType],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__SOLID_NUMERICS_MECHANICAL_TIME_INTEGRATION_TYPE_VARIANTS,
        )
    ),
]
