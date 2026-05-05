from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.length import Length


class MoveFacesGroupParameter(SimScaleModel):
    selected: Literal["move_faces_mode_distance", "move_faces_mode_to_entity"] = Field(
        description="Defines the parameter set used to define the extrusion. It can be either: - `move_faces_mode_distance`, in which case the move distance will be provided, or - `move_faces_mode_to_entity`, in which case the move distance will be computed based on the provided face."
    )
    move_distance: Length | None = Field(default=None)
    move_up_to_face: str | None = Field(default=None, description="Face limiting the move.")
