from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.entity_assignment_source import EntityAssignmentSource


class EntityAssignmentList(SimScaleModel):
    """(A multi-select) geometric entity assignment list."""

    entities: list[str] | None = Field(default=None)
    saved_selections: list[str] | None = Field(
        validation_alias="savedSelections", serialization_alias="savedSelections", default=None
    )
    source: EntityAssignmentSource | None = Field(default=None)
