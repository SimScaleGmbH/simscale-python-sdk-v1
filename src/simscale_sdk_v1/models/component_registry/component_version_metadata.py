from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ComponentVersionMetadata(SimScaleModel):
    """Encapsulates all generic metadata about a component at a particular version."""

    component_version_reference: str | None = Field(
        validation_alias="componentVersionReference",
        serialization_alias="componentVersionReference",
        default=None,
        description="Reference to a component version.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  Component versions follow the convention of semantic versioning.  The fully qualified reference of a component version follows the following syntax: `[component_group]:[component]:[component_version]`.",
    )
    description: str | None = Field(default=None)
    multi_language_description: dict[str, str] | None = Field(
        validation_alias="multiLanguageDescription", serialization_alias="multiLanguageDescription", default=None
    )
    multi_language_name: dict[str, str] | None = Field(
        validation_alias="multiLanguageName", serialization_alias="multiLanguageName", default=None
    )
    name: str | None = Field(default=None)
    state: Literal["SNAPSHOT", "RELEASE_CANDIDATE", "RELEASED", "DEPRECATED", "ARCHIVED"] | None = Field(
        default=None, description="Possible states of a component version."
    )
