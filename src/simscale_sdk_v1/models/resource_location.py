from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ResourceLocation(SimScaleModel):
    """Specify the destination to which the resource will be moved/copied"""

    space_id: str = Field(validation_alias="spaceId", serialization_alias="spaceId")
    parent_folder_id: str | None = Field(
        validation_alias="parentFolderId",
        serialization_alias="parentFolderId",
        default=None,
        description="If missing, the resource will be moved/copied to the root of the Space",
    )
