from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.material.material_properties import MaterialProperties


class MaterialResponse(SimScaleModel):
    id: str = Field(description="The material unique identifier.")
    material_group_id: str = Field(
        validation_alias="materialGroupId",
        serialization_alias="materialGroupId",
        description="The material group unique identifier.",
    )
    name: str = Field(description="The material name.")
    created_at: datetime = Field(
        validation_alias="createdAt", serialization_alias="createdAt", description="The time the material was created."
    )
    modified_at: datetime = Field(
        validation_alias="modifiedAt",
        serialization_alias="modifiedAt",
        description="The time the material was modified.",
    )
    properties: MaterialProperties | None = Field(default=None)
    metadata: dict[str, Any] | None = Field(default=None)
