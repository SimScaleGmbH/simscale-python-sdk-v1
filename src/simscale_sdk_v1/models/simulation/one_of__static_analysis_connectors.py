from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.bolt_connector import BoltConnector
from simscale_sdk_v1.models.simulation.pin_connector import PinConnector

_ONE_OF__STATIC_ANALYSIS_CONNECTORS_VARIANTS: dict[str, type] = {
    "PIN_CONNECTOR": PinConnector,
    "BOLT_CONNECTOR": BoltConnector,
}

OneOf_StaticAnalysisConnectors = Annotated[
    Union[PinConnector, BoltConnector],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__STATIC_ANALYSIS_CONNECTORS_VARIANTS,
        )
    ),
]
