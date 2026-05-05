from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.space_settings import SpaceSettings


class Space(SimScaleModel):
    space_id: str | None = Field(validation_alias="spaceId", serialization_alias="spaceId", default=None)
    organization_id: str | None = Field(
        validation_alias="organizationId",
        serialization_alias="organizationId",
        default=None,
        description="Only present for Team Spaces",
    )
    owner_username: str | None = Field(
        validation_alias="ownerUsername",
        serialization_alias="ownerUsername",
        default=None,
        description="Only present for Personal Spaces",
    )
    space_type: Literal["PERSONAL", "TEAM"] | None = Field(
        validation_alias="spaceType", serialization_alias="spaceType", default=None
    )
    name: str | None = Field(default=None)
    created_at: datetime | None = Field(validation_alias="createdAt", serialization_alias="createdAt", default=None)
    last_modified_at: datetime | None = Field(
        validation_alias="lastModifiedAt", serialization_alias="lastModifiedAt", default=None
    )
    space_settings: SpaceSettings | None = Field(
        validation_alias="spaceSettings", serialization_alias="spaceSettings", default=None
    )
