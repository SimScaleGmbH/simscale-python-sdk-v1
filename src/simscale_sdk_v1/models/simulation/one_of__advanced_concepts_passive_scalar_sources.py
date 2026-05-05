from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.absolute_passive_scalar_source import AbsolutePassiveScalarSource
from simscale_sdk_v1.models.simulation.specific_passive_scalar_source import SpecificPassiveScalarSource

_ONE_OF__ADVANCED_CONCEPTS_PASSIVE_SCALAR_SOURCES_VARIANTS: dict[str, type] = {
    "ABSOLUTE": AbsolutePassiveScalarSource,
    "SPECIFIC": SpecificPassiveScalarSource,
}

OneOf_AdvancedConceptsPassiveScalarSources = Annotated[
    Union[AbsolutePassiveScalarSource, SpecificPassiveScalarSource],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ADVANCED_CONCEPTS_PASSIVE_SCALAR_SOURCES_VARIANTS,
        )
    ),
]
