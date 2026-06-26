from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.entity_assignment_source import EntityAssignmentSource


class EntityAssignment(SimScaleModel):
    """(A single-select) entity assignment from an arbitrary source (CAD/Mesh)."""

    entity: str | None = Field(default=None)
    saved_selection: str | None = Field(
        validation_alias="savedSelection", serialization_alias="savedSelection", default=None
    )
    source: EntityAssignmentSource | None = Field(default=None)
