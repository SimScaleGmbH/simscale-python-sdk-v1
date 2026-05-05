from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CollectionLinks(SimScaleModel):
    first: Any | None = Field(default=None)
    prev: Any | None = Field(default=None)
    self: Any | None = Field(default=None)
    next: Any | None = Field(default=None)
    last: Any | None = Field(default=None)
