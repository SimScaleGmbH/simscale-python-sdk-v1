from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.entity_assignment_list import EntityAssignmentList


class EntityAssignmentListConstant(SimScaleModel):
    entity_assignment_list: EntityAssignmentList | None = Field(
        validation_alias="entityAssignmentList", serialization_alias="entityAssignmentList", default=None
    )
    value_model_type: str
