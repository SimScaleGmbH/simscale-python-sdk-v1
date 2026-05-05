from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.box_with_unit import BoxWithUnit


class CreateBoxMethod(SimScaleModel):
    """Defines how the box is created."""

    selected: Literal["create-box-from-definition", "create-box-from-faces"] = Field(
        description="Defines the parameter set used to define the box. It can be either: - `create-box-from-definition`, in which case the `box` parameter needs to be defined, or - `create-box-from-faces`, in which case the `faces` parameter needs to be defined with appropriate scaling."
    )
    box: BoxWithUnit | None = Field(default=None)
    faces: list[str] | None = Field(
        default=None, description="List of faces. This parameter is only valid for `create-box-from-faces` mode."
    )
    scaling_factor: float | None = Field(
        default=None,
        description="Scaling factor to apply to the box, if none is provided the box will fit the input faces. This parameter is only valid for `create-box-from-faces` mode.",
    )
