from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Folder(SimScaleModel):
    resource_type: Literal["PROJECT", "FOLDER"] | None = Field(
        validation_alias="resourceType", serialization_alias="resourceType", default="FOLDER"
    )
    folder_id: str | None = Field(validation_alias="folderId", serialization_alias="folderId", default=None)
    parent_folder_id: str | None = Field(
        validation_alias="parentFolderId",
        serialization_alias="parentFolderId",
        default=None,
        description="Can be missing if the folder is at the root level of the Space",
    )
    space_id: str | None = Field(validation_alias="spaceId", serialization_alias="spaceId", default=None)
    name: str
    number_of_items: int | None = Field(
        validation_alias="numberOfItems", serialization_alias="numberOfItems", default=None
    )
    created_at: datetime | None = Field(validation_alias="createdAt", serialization_alias="createdAt", default=None)
    last_modified_at: datetime | None = Field(
        validation_alias="lastModifiedAt", serialization_alias="lastModifiedAt", default=None
    )
