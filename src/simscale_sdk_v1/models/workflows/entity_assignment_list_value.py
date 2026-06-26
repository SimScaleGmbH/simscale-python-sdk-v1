from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.entity_assignment_list_constant import EntityAssignmentListConstant
from simscale_sdk_v1.models.workflows.entity_assignment_list_from_components import EntityAssignmentListFromComponents
from simscale_sdk_v1.models.workflows.entity_assignment_list_intersect import EntityAssignmentListIntersect
from simscale_sdk_v1.models.workflows.entity_assignment_list_map_entities import EntityAssignmentListMapEntities
from simscale_sdk_v1.models.workflows.entity_assignment_list_reference import EntityAssignmentListReference
from simscale_sdk_v1.models.workflows.entity_assignment_to_entity_assignment_list_value_conversion import (
    EntityAssignmentToEntityAssignmentListValueConversion,
)

# Value model for an entity assignment list. Resolves to an object node following the [EntityAssignmentList] data model.
_ENTITY_ASSIGNMENT_LIST_VALUE_VARIANTS: dict[str, type] = {
    "entity_assignment:conversion:to_entity_assignment_list": EntityAssignmentToEntityAssignmentListValueConversion,
    "entity_assignment_list:constant": EntityAssignmentListConstant,
    "entity_assignment_list:function:intersect": EntityAssignmentListIntersect,
    "entity_assignment_list:function:map_entities": EntityAssignmentListMapEntities,
    "entity_assignment_list:reference": EntityAssignmentListReference,
    "list:conversion:to_entity_assignment_list": EntityAssignmentListFromComponents,
}

EntityAssignmentListValue = Annotated[
    Union[
        EntityAssignmentToEntityAssignmentListValueConversion,
        EntityAssignmentListConstant,
        EntityAssignmentListIntersect,
        EntityAssignmentListMapEntities,
        EntityAssignmentListReference,
        EntityAssignmentListFromComponents,
    ],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_model_type",
            variants=_ENTITY_ASSIGNMENT_LIST_VALUE_VARIANTS,
        )
    ),
]
