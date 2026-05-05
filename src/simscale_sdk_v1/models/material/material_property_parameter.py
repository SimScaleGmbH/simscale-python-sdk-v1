from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class MaterialPropertyParameter(SimScaleModel):
    key: str = Field(
        description="The unique identifier of the parameter, meaningful from the physics/business perspective"
    )
    name: str | None = Field(
        default=None, description="Optional user facing name or label key for human identification"
    )
    unit: str | None = Field(default=None, description="The parameter unit")
