from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.material.material_group_type import MaterialGroupType


class MaterialGroupResponse(SimScaleModel):
    material_group_id: str = Field(
        validation_alias="materialGroupId",
        serialization_alias="materialGroupId",
        description="The ID of the material group.",
    )
    parent_id: str | None = Field(
        validation_alias="parentId",
        serialization_alias="parentId",
        default=None,
        description="The ID of parent of the material group.",
    )
    name: str = Field(description="The name of the material group.")
    group_type: MaterialGroupType | None = Field(
        validation_alias="groupType", serialization_alias="groupType", default=None
    )
    created_at: datetime = Field(
        validation_alias="createdAt",
        serialization_alias="createdAt",
        description="The time the material group was created.",
    )
    modified_at: datetime = Field(
        validation_alias="modifiedAt",
        serialization_alias="modifiedAt",
        description="The time the material group was modified.",
    )
    metadata: dict[str, Any] | None = Field(default=None, description="Material group metadata.")
