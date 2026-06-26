from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class StringUpperCaseFunction(SimScaleModel):
    string: Any | None = Field(
        default=None, description="Value model for a string value. Resolves to a text JSON node."
    )
    value_model_type: str
