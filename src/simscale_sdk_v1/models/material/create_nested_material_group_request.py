from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateNestedMaterialGroupRequest(SimScaleModel):
    name: str = Field(description="The name of the material group.")
    metadata: dict[str, Any] | None = Field(default=None)
