from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SimplifyParameters(SimScaleModel):
    occurrences: list[str] | None = Field(default=None, description="List of solid regions and/or sheet bodies.")
    primitive: Literal["box", "cylinder"] = Field(
        description="Type of body used in the simplification. It can be either: `box`, or `cylinder`."
    )
    replace_each: bool = Field(
        description="Controls the result. If `true`, each body will be replaced singularly; otherwise all bodies will be replaced by a single primitive."
    )
