from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class ErrorParameter(SimScaleModel):
    name: str | None = Field(default=None)
    type_: Literal["TEXT", "NUMBER", "DATE", "LIST"] | None = Field(
        validation_alias="type", serialization_alias="type", default=None
    )
    value: Any | None = Field(default=None)
