from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.box_with_unit import BoxWithUnit


class CreateBoxMethod(SimScaleModel):
    """Defines how the box is created."""

    selected: Literal["create-box-from-definition", "create-box-from-faces"] = Field(
        description="Defines how the box should be created. It can be either: - `create-box-from-definition`, in which case the `box` parameter needs to be defined, including min/max corner coordinates and a unit, or - `create-box-from-faces`, in which case the `faces` parameter needs to be defined, with an optional `scaling_factor`."
    )
    box: BoxWithUnit | None = Field(default=None)
    faces: list[str] | None = Field(
        default=None,
        description="List of faces used to fit the box. This parameter is only valid for `create-box-from-faces` mode.",
    )
    scaling_factor: float | None = Field(
        default=None,
        description="Optional scale factor applied to the fitted box. If omitted, the box fits the selected faces. This parameter is only valid for `create-box-from-faces` mode.",
    )
