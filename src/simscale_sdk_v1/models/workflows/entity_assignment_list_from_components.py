from __future__ import annotations

from typing import Any
from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EntityAssignmentListFromComponents(SimScaleModel):
    entities: Any | None = Field(
        default=None, description="Value model for a list of values. Resolves to a JSON array."
    )
    source: Any | None = Field(
        default=None, description="Value model for a string value. Resolves to a text JSON node."
    )
    source_type: Literal["CAD", "MESH"] | None = Field(
        validation_alias="sourceType",
        serialization_alias="sourceType",
        default="",
        description="Source type is either CAD (model) or mesh.",
    )
    value_model_type: str
