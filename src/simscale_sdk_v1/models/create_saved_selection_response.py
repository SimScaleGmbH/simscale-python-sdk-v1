from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CreateSavedSelectionResponse(SimScaleModel):
    cad_state_id: str | None = Field(
        validation_alias="cadStateId",
        serialization_alias="cadStateId",
        default=None,
        description="ID of the newly created CAD state.",
    )
    saved_selection_id: str | None = Field(
        validation_alias="savedSelectionId",
        serialization_alias="savedSelectionId",
        default=None,
        description="ID of the newly created saved selection.",
    )
