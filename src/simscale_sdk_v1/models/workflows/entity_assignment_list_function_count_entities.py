from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EntityAssignmentListFunctionCountEntities(SimScaleModel):
    entity_assignment_list_value: Any | None = Field(
        validation_alias="entityAssignmentListValue",
        serialization_alias="entityAssignmentListValue",
        default=None,
        description="Value model for an entity assignment list. Resolves to an object node following the [EntityAssignmentList] data model.",
    )
    value_model_type: str
