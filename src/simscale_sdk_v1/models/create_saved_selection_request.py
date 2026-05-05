from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.saved_selection_type import SavedSelectionType


class CreateSavedSelectionRequest(SimScaleModel):
    name: str = Field(description="The name of the saved selection.")
    type_: SavedSelectionType = Field(validation_alias="type", serialization_alias="type")
    entities: list[str] = Field(description="The entities included in the saved selection.")
