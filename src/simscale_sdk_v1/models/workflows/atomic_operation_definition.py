from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.inline_operation_definition import InlineOperationDefinition
from simscale_sdk_v1.models.workflows.method_operation_definition import MethodOperationDefinition
from simscale_sdk_v1.models.workflows.nested_workflow_operation_definition import NestedWorkflowOperationDefinition

# Atomic workflow operation which can be executed as is without further decomposition by the workflow engine.  It can either refer to a method or a nested workflow.
_ATOMIC_OPERATION_DEFINITION_VARIANTS: dict[str, type] = {
    "inline": InlineOperationDefinition,
    "method": MethodOperationDefinition,
    "workflow": NestedWorkflowOperationDefinition,
}

AtomicOperationDefinition = Annotated[
    Union[InlineOperationDefinition, MethodOperationDefinition, NestedWorkflowOperationDefinition],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="operation_definition_type",
            variants=_ATOMIC_OPERATION_DEFINITION_VARIANTS,
        )
    ),
]
