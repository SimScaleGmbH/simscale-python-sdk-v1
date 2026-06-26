from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StringExpressionSelect(SimScaleModel):
    options: list[dict[str, Any]] | None = Field(default=None)
    value_model_type: str
