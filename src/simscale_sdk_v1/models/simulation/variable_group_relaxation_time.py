from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__time import Unit_Time


class VariableGroup_RELAXATION_TIME(SimScaleModel):
    r_t: Unit_Time | None = Field(validation_alias="R_T", serialization_alias="R_T", default=None)
