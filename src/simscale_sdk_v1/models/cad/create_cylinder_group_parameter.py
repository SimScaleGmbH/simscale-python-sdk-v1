from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.cylinder import Cylinder


class CreateCylinderGroupParameter(SimScaleModel):
    selected: Literal["create-cylinder-from-definition", "create-cylinder-from-faces"] = Field(
        description="Defines how the cylinder should be created. It can be either: - `create-cylinder-from-definition`, in which case the `cylinder` parameter needs to be defined, including center, axis, radius, and height, or - `create-cylinder-from-faces`, in which case the `faces` parameter needs to be defined. The cylinder will be fitted to enclose only those selected faces, with optional `radial_clearance_factor` and `height_clearance_factor` scale factors to adjust the fit."
    )
    faces: list[str] | None = Field(
        default=None,
        description="List of faces used to fit the cylinder. This parameter is only valid for `create-cylinder-from-faces` mode.",
    )
    radial_clearance_factor: float | None = Field(
        default=None,
        description="Optional scale factor applied to the fitted cylinder radius. If omitted, the radius fits the selected faces. This parameter is only valid for `create-cylinder-from-faces` mode.",
    )
    height_clearance_factor: float | None = Field(
        default=None,
        description="Optional scale factor applied to the fitted cylinder height. If omitted, the height fits the selected faces. This parameter is only valid for `create-cylinder-from-faces` mode.",
    )
    cylinder: Cylinder | None = Field(default=None)
