from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EntityAssignmentToEntityAssignmentListValueConversion(SimScaleModel):
    entity_assignment_value: Any | None = Field(
        validation_alias="entityAssignmentValue",
        serialization_alias="entityAssignmentValue",
        default=None,
        description="Value model for an entity assignment. Resolves to an object node following the [EntityAssignment] data model.",
    )
    value_model_type: str
