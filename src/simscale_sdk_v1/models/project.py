from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class Project(SimScaleModel):
    project_id: str | None = Field(validation_alias="projectId", serialization_alias="projectId", default=None)
    space_id: str | None = Field(
        validation_alias="spaceId",
        serialization_alias="spaceId",
        default=None,
        description="Always returned by the backend. Optional at project creation. If missing, the project will be created in the Personal Space of the user.",
    )
    parent_folder_id: str | None = Field(
        validation_alias="parentFolderId",
        serialization_alias="parentFolderId",
        default=None,
        description="If missing, the project is located at the root level of the Space.",
    )
    created_at: datetime | None = Field(validation_alias="createdAt", serialization_alias="createdAt", default=None)
    name: str = Field(
        description="The project title should contain the application you want to analyze as well as the simulation method you want to use, e.g. 'Heat exchanger - CHT simulation'."
    )
    description: str | None = Field(default=None, description="A meaningful description of the project.")
    measurement_system: Literal["SI", "US_CUSTOMARY"] = Field(
        validation_alias="measurementSystem",
        serialization_alias="measurementSystem",
        default="SI",
        description="The measurement system of the project. Can't be modified.",
    )
    tags: list[str] | None = Field(default=None)
