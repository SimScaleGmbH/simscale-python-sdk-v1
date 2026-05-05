from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class DeleteFaceV2Parameters(SimScaleModel):
    faces: list[str] | None = Field(default=None, description="List of faces.")
    heal_action: Literal["cap", "shrink", "no"] = Field(
        description="The available healing actions are: - `cap`: to replace deleted faces with a new face, - `shrink` to extend the neighboring faces to cover the hole left by the deleted face, - `no`: to simply removes the faces, thus potentially converting solid bodies into sheet bodies."
    )
