from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateUploadSessionRequest(SimScaleModel):
    """Request to initialize an upload session backed by pre-signed URLs."""

    content_type: str | None = Field(validation_alias="contentType", serialization_alias="contentType", default=None)
    data_type: str | None = Field(
        validation_alias="dataType",
        serialization_alias="dataType",
        default=None,
        description="Reference to a component version.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  Component versions follow the convention of semantic versioning.  The fully qualified reference of a component version follows the following syntax: `[component_group]:[component]:[component_version]`.",
    )
