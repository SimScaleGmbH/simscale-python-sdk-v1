from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateMaterialGroupRequest(SimScaleModel):
    name: str = Field(description="The name of the material group.")
    metadata: dict[str, Any] | None = Field(default=None)
    team_group_id: int | None = Field(
        validation_alias="teamGroupId",
        serialization_alias="teamGroupId",
        default=None,
        description="The material group will be assigned to this team group id. This field can only be used by support group members.",
    )
