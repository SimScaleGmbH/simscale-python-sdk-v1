from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class EntityAssignmentSource(SimScaleModel):
    """Entity assignment source is represented by its input data ID and its type (CAD or MESH)."""

    input_data_name: str | None = Field(
        validation_alias="inputDataName", serialization_alias="inputDataName", default=None
    )
    type_: Literal["CAD", "MESH"] | None = Field(
        validation_alias="type",
        serialization_alias="type",
        default="",
        description="Source type is either CAD (model) or mesh.",
    )
