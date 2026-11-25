from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__advanced_marc_numerics_settings_marc_stabilization import (
    OneOf_AdvancedMarcNumericsSettingsMarcStabilization,
)


class AdvancedMarcNumericsSettings(SimScaleModel):
    marc_stabilization: OneOf_AdvancedMarcNumericsSettingsMarcStabilization | None = Field(
        validation_alias="marcStabilization", serialization_alias="marcStabilization", default=None
    )
