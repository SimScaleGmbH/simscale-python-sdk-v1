from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.extrude_by_parameter import ExtrudeByParameter


class ExtrudeFacesParameters(SimScaleModel):
    faces: list[str] | None = Field(default=None, description="List of faces.")
    extrude_method: Literal["merge", "remove", "add_new"] = Field(
        description="The available extrude methods are: - `merge`: to merge the extrusion back to the original body, - `remove`: to extrude in the negative normal direction and subtract the result from the original body, - `add_new`: to save the extrusion as a new body in the CAD."
    )
    extrude_by: ExtrudeByParameter
