from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad_feature import CadFeature
from simscale_sdk_v1.models.cad_internal_format import CadInternalFormat
from simscale_sdk_v1.models.saved_selection import SavedSelection


class CadState(SimScaleModel):
    name: str | None = Field(default=None, description="Name of the CAD state.")
    format: CadInternalFormat | None = Field(default=None)
    faults: dict[str, Any] | None = Field(default=None, description="Faults in the CAD.")
    saved_selections: list[SavedSelection] | None = Field(
        validation_alias="savedSelections",
        serialization_alias="savedSelections",
        default=None,
        description="List of saved selections in the CAD state.",
    )
    features: list[CadFeature] | None = Field(default=None, description="List of features in the CAD state.")
