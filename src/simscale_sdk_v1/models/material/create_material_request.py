from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.material.material_properties import MaterialProperties


class CreateMaterialRequest(SimScaleModel):
    name: str = Field(description="The material name.")
    metadata: dict[str, Any] | None = Field(default=None)
    properties: MaterialProperties
