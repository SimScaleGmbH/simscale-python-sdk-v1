from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.plane import Plane


class SplitBodiesParameters(SimScaleModel):
    split_mode: Literal["plane", "face"] | None = Field(
        default=None,
        description="Defines how the split plane is specified. It can be either: - `plane` (default if omitted), in which case the `plane` parameter needs to be defined, or - `face`, in which case the `face` parameter needs to be defined. The bodies are split by the plane of the selected planar face.",
    )
    plane: Plane | None = Field(default=None)
    face: str | None = Field(
        default=None,
        description="Planar face whose plane specifies where the split occurs. Required in `face` mode, ignored in `plane` mode.",
    )
    reverse_face_normal: bool | None = Field(
        default=None,
        description="If `true`, the normal of the selected face is reversed, so the other side is retained when `keep_both` is `false`. Only used in `face` mode, defaults to `false`.",
    )
    keep_both: bool = Field(
        description="Controls the split. If `true`, both sides of the bodies are kept; otherwise, only the side facing the normal is retained."
    )
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
