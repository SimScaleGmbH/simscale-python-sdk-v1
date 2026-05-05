from __future__ import annotations

from datetime import datetime

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad_internal_format import CadInternalFormat


class Cad(SimScaleModel):
    cad_id: str | None = Field(
        validation_alias="cadId", serialization_alias="cadId", default=None, description="The ID of the CAD."
    )
    cad_state_id: str | None = Field(
        validation_alias="cadStateId",
        serialization_alias="cadStateId",
        default=None,
        description="The ID of the current CAD state.",
    )
    name: str | None = Field(default=None, description="The name of the CAD.")
    created_at: datetime | None = Field(
        validation_alias="createdAt",
        serialization_alias="createdAt",
        default=None,
        description="The time when the CAD was imported.",
    )
    format: CadInternalFormat | None = Field(default=None)
