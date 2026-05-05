from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__frequency import Unit_Frequency


class VariableGroup_F(SimScaleModel):
    f: Unit_Frequency | None = Field(validation_alias="F", serialization_alias="F", default=None)
