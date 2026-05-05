from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SubtractBodiesParameters(SimScaleModel):
    targets: list[str] | None = Field(default=None, description="List of target solid regions and/or sheet bodies.")
    tools: list[str] | None = Field(default=None, description="List of tool solid regions and/or sheet bodies.")
    keep_tools: Literal["keep", "discard"] = Field(
        description="Controls the result. If `keep`, both parts if the target bodies are kept after the subtraction; otherwise, if `discard` only the non intersection part wil be retained."
    )
