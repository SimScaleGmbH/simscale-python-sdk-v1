from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class RenameCadResponse(SimScaleModel):
    cad_state_id: str | None = Field(
        validation_alias="cadStateId",
        serialization_alias="cadStateId",
        default=None,
        description="ID of the newly created CAD state.",
    )
