from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.entity_assignment import EntityAssignment


class EntityAssignmentConstant(SimScaleModel):
    entity_assignment: EntityAssignment | None = Field(
        validation_alias="entityAssignment", serialization_alias="entityAssignment", default=None
    )
    value_model_type: str
