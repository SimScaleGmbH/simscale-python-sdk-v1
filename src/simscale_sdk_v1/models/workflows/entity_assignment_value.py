from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.workflows.entity_assignment_constant import EntityAssignmentConstant
from simscale_sdk_v1.models.workflows.entity_assignment_map_entities import EntityAssignmentMapEntities
from simscale_sdk_v1.models.workflows.entity_assignment_reference import EntityAssignmentReference

# Value model for an entity assignment. Resolves to an object node following the [EntityAssignment] data model.
_ENTITY_ASSIGNMENT_VALUE_VARIANTS: dict[str, type] = {
    "entity_assignment:constant": EntityAssignmentConstant,
    "entity_assignment:function:map_entities": EntityAssignmentMapEntities,
    "entity_assignment:reference": EntityAssignmentReference,
}

EntityAssignmentValue = Annotated[
    Union[EntityAssignmentConstant, EntityAssignmentMapEntities, EntityAssignmentReference],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="value_model_type",
            variants=_ENTITY_ASSIGNMENT_VALUE_VARIANTS,
        )
    ),
]
