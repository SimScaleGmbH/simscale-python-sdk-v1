from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.simulation.automatic_element_definition_method import AutomaticElementDefinitionMethod
from simscale_sdk_v1.models.simulation.custom_element_definition_method import CustomElementDefinitionMethod

_ONE_OF__ELEMENT_TECHNOLOGY_DEFINITION_METHOD_VARIANTS: dict[str, type] = {
    "AUTOMATIC": AutomaticElementDefinitionMethod,
    "CUSTOM": CustomElementDefinitionMethod,
}

OneOf_ElementTechnologyDefinitionMethod = Annotated[
    Union[AutomaticElementDefinitionMethod, CustomElementDefinitionMethod],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="type",
            variants=_ONE_OF__ELEMENT_TECHNOLOGY_DEFINITION_METHOD_VARIANTS,
        )
    ),
]
