from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CollectionMeta(SimScaleModel):
    total: int | None = Field(default=None, description="Total number of resources in the collection.")
