from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DeleteFaceV2Parameters(SimScaleModel):
    faces: list[str] | None = Field(default=None, description="List of faces.")
    heal_action: Literal["cap", "shrink", "no"] = Field(
        description="The available healing actions are: - `cap`: replaces deleted faces with a new face, - `shrink`: closes the hole left by the deleted face by extending the neighboring faces to cover it, - `no`: removes the faces, converting solid bodies into sheet bodies."
    )
