from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.length import Length


class ExtrudeByParameter(SimScaleModel):
    selected: Literal["extrude_faces_mode_distance", "extrude_faces_mode_to_entity"] = Field(
        description="Defines the parameter set used to define the extrusion. It can be either: - `extrude_faces_mode_distance`, in which case the extrusion distance will be provided, or - `extrude_faces_mode_to_entity`, in which case the extrusion distance will be computed based on the provided face."
    )
    extrude_distance: Length | None = Field(default=None)
    extrude_up_to_face: str | None = Field(default=None, description="Face limiting the extrusion.")
