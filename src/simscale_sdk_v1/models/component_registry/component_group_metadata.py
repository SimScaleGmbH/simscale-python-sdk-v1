from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ComponentGroupMetadata(SimScaleModel):
    """Data for fetching information about component groups. Contains all properties which are accessible by clients."""

    component_group_reference: str | None = Field(
        validation_alias="componentGroupReference",
        serialization_alias="componentGroupReference",
        default=None,
        description="Reference to a component group.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid name collisions and also to group components semantically.  It is expressed as a string where the levels are separated with a dot (`.`).",
    )
    description: str | None = Field(default=None)
    has_children: bool | None = Field(validation_alias="hasChildren", serialization_alias="hasChildren", default=None)
    multi_language_description: dict[str, str] | None = Field(
        validation_alias="multiLanguageDescription", serialization_alias="multiLanguageDescription", default=None
    )
    multi_language_name: dict[str, str] | None = Field(
        validation_alias="multiLanguageName", serialization_alias="multiLanguageName", default=None
    )
    name: str | None = Field(default=None)
    state: Literal["ACTIVE", "ARCHIVED"] | None = Field(
        default=None, description="Possible states of a component group."
    )
