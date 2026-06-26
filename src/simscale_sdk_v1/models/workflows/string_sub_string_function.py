from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.workflows.string_value import StringValue


class StringSubStringFunction(SimScaleModel):
    from_: Any | None = Field(
        validation_alias="from",
        serialization_alias="from",
        default=None,
        description="Value model for a 64-bit signed integer value. Resolves to a long JSON node.",
    )
    string: StringValue | None = Field(default=None)
    to: Any | None = Field(
        default=None, description="Value model for a 64-bit signed integer value. Resolves to a long JSON node."
    )
