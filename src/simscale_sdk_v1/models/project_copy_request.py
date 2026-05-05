from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ProjectCopyRequest(SimScaleModel):
    space_id: str | None = Field(
        validation_alias="spaceId",
        serialization_alias="spaceId",
        default=None,
        description="If missing, the project will be copied in the Personal Space of the user.",
    )
    parent_folder_id: str | None = Field(
        validation_alias="parentFolderId",
        serialization_alias="parentFolderId",
        default=None,
        description="If missing, the project is located at the root level of the Space.",
    )
    name: str = Field(
        description="The project title should contain the application you want to analyze as well as the simulation method you want to use, e.g. 'Heat exchanger - CHT simulation'."
    )
    description: str = Field(description="A meaningful description of the project.")
