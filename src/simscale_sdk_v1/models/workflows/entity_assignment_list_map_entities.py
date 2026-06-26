from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.entity_assignment_source import EntityAssignmentSource


class EntityAssignmentListMapEntities(SimScaleModel):
    entity_assignment_list_value: Any | None = Field(
        validation_alias="entityAssignmentListValue",
        serialization_alias="entityAssignmentListValue",
        default=None,
        description="Value model for an entity assignment list. Resolves to an object node following the [EntityAssignmentList] data model.",
    )
    target_assignment_source: EntityAssignmentSource | None = Field(
        validation_alias="targetAssignmentSource", serialization_alias="targetAssignmentSource", default=None
    )
    value_model_type: str
