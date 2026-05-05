from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.original_entity_reference import OriginalEntityReference


class EntityDescription(SimScaleModel):
    name: str | None = Field(default=None, description="The internal name of the entity.")
    class_: str | None = Field(
        validation_alias="class",
        serialization_alias="class",
        default=None,
        description="The topological entity class (body or face).",
    )
    originate_from: list[OriginalEntityReference] | None = Field(
        validation_alias="originateFrom", serialization_alias="originateFrom", default=None
    )
