from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__dimensionless import Unit_Dimensionless


class VariableGroup_STRAIN(SimScaleModel):
    e: Unit_Dimensionless | None = Field(validation_alias="E", serialization_alias="E", default=None)
