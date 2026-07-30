from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class SubtractBodiesParameters(SimScaleModel):
    targets: list[str] | None = Field(default=None, description="List of target solid regions and/or sheet bodies.")
    tools: list[str] | None = Field(default=None, description="List of tool solid regions and/or sheet bodies.")
    keep_tools: Literal["keep", "discard"] = Field(
        description="Controls whether the tool bodies are retained after the subtraction. If `keep`, the tool bodies are kept alongside the resulting target bodies; if `discard`, the tool bodies are removed and only the resulting target bodies are retained."
    )
