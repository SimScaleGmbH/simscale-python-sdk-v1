from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.saved_selection_type import SavedSelectionType


class SavedSelection(SimScaleModel):
    id: str | None = Field(default=None, description="The ID of the saved selection.")
    name: str | None = Field(default=None, description="The name of the saved selection.")
    type_: SavedSelectionType | None = Field(validation_alias="type", serialization_alias="type", default=None)
    entities: list[str] | None = Field(default=None)
