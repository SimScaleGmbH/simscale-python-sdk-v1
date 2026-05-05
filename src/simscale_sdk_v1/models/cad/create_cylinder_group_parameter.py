from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.cylinder import Cylinder


class CreateCylinderGroupParameter(SimScaleModel):
    selected: Literal["create-cylinder-from-definition", "create-cylinder-from-faces"] = Field(
        description="Defines the parameter set used to define the cylinder. It can be either: - `create-cylinder-from-definition`, in which case the `cylinder` parameter needs to be defined, or - `create-cylinder-from-faces`, in which case the `faces` parameter needs to be defined with appropriate factors."
    )
    faces: list[str] | None = Field(
        default=None, description="List of faces. This parameter is only valid for `create-cylinder-from-faces` mode."
    )
    radial_clearance_factor: float | None = Field(
        default=None,
        description="Scaling factor to apply to the radius of the cylinder, if none is provided the radius will fit the input faces. This parameter is only valid for `create-cylinder-from-faces` mode.",
    )
    height_clearance_factor: float | None = Field(
        default=None,
        description="Scaling factor to apply to the height of the cylinder, if none is provided the height will fit the input faces. This parameter is only valid for `create-cylinder-from-faces` mode.",
    )
    cylinder: Cylinder | None = Field(default=None)
