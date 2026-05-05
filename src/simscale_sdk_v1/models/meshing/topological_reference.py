from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TopologicalReference(SimScaleModel):
    entities: list[str] | None = Field(default=None)
    sets: list[str] | None = Field(default=None)
