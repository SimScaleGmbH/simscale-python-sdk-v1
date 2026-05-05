from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.body_path import BodyPath
from simscale_sdk_v1.models.entity_attribute import EntityAttribute


class OriginalEntityReference(SimScaleModel):
    path: list[BodyPath] | None = Field(default=None, description="The path from the root of the model.")
    body: str | None = Field(default=None, description="The original body name.")
    entity: str | None = Field(default=None, description="The original entity name.")
    attribute_list: list[EntityAttribute] | None = Field(
        validation_alias="attributeList",
        serialization_alias="attributeList",
        default=None,
        description="The attributes assigned to the entity.",
    )
