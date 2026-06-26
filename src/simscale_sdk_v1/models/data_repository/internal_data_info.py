from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class InternalDataInfo(SimScaleModel):
    content_type: str | None = Field(validation_alias="contentType", serialization_alias="contentType", default=None)
    created_by: int | None = Field(validation_alias="createdBy", serialization_alias="createdBy", default=None)
    creation_timestamp: datetime | None = Field(
        validation_alias="creationTimestamp", serialization_alias="creationTimestamp", default=None
    )
    data_id: str | None = Field(
        validation_alias="dataId",
        serialization_alias="dataId",
        default=None,
        description="Data identifier. It is a string composed of the type identifier and a UUID: `data:[UUID]`.",
    )
    data_provider_type: Literal["INTERNAL", "EXTERNAL"] | None = Field(
        validation_alias="dataProviderType",
        serialization_alias="dataProviderType",
        default=None,
        description="Identifies if a data is - `INTERNAL`: data is stored and managed by `data-repository` service or - `EXTERNAL`: data is stored and managed by an external service. Only a reference for it is stored in `data-repository` service.",
    )
    data_size: int | None = Field(validation_alias="dataSize", serialization_alias="dataSize", default=None)
    data_type: str | None = Field(
        validation_alias="dataType",
        serialization_alias="dataType",
        default=None,
        description="Reference to a component version.  Components are organized into a group hierarchy which serves as a qualification mechanism to avoid collisions and also to group components semantically.  Component versions follow the convention of semantic versioning.  The fully qualified reference of a component version follows the following syntax: `[component_group]:[component]:[component_version]`.",
    )
    data_info_type: str
    origin: Literal["USER_UPLOAD", "WORKFLOW_EXECUTION"] | None = Field(
        default=None,
        description="Identifies the origin of data creation: - `USER_UPLOAD`: data was uploaded or registered directly by a user through the API - `WORKFLOW_EXECUTION`: data was created as a result of a workflow run",
    )
    project_id: str | None = Field(validation_alias="projectId", serialization_alias="projectId", default=None)
    storage_id: str | None = Field(validation_alias="storageId", serialization_alias="storageId", default=None)
