from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.move_faces_group_parameter import MoveFacesGroupParameter


class MoveFacesParameters(SimScaleModel):
    faces: list[str] | None = Field(default=None, description="List of faces.")
    move_method: MoveFacesGroupParameter
