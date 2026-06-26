from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.input_data_definition import InputDataDefinition
from simscale_sdk_v1.models.workflows.intermediate_data_definition import IntermediateDataDefinition
from simscale_sdk_v1.models.workflows.output_data_definition import OutputDataDefinition

# Abstract workflow data definition.  It can be either: * input data of the workflow * output data of the workflow * other intermediate data in the workflow
_ABSTRACT_DATA_DEFINITION_VARIANTS: dict[str, type] = {
    "input": InputDataDefinition,
    "intermediate": IntermediateDataDefinition,
    "output": OutputDataDefinition,
}

AbstractDataDefinition = Annotated[
    Union[InputDataDefinition, IntermediateDataDefinition, OutputDataDefinition],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="data_definition_type",
            variants=_ABSTRACT_DATA_DEFINITION_VARIANTS,
        )
    ),
]
