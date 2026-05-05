from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__magnetic_field_strength import Unit_MagneticFieldStrength


class VariableGroup_MAGNETIC_FIELD_STRENGTH(SimScaleModel):
    h: Unit_MagneticFieldStrength | None = Field(validation_alias="H", serialization_alias="H", default=None)
