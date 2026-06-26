from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class OrganizationComponentGroupMetadata(SimScaleModel):
    """Metadata of an organization component group."""

    name: str | None = Field(default=None)
    organization_component_group_reference: str | None = Field(
        validation_alias="organizationComponentGroupReference",
        serialization_alias="organizationComponentGroupReference",
        default=None,
        description="Reference to a component group.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid name collisions and also to group components semantically.  It is expressed as a string where the levels are separated with a dot (`.`).",
    )
    organization_id: str | None = Field(
        validation_alias="organizationId", serialization_alias="organizationId", default=None
    )
