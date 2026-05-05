from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.unit__dimensionless import Unit_Dimensionless
from simscale_sdk_v1.models.simulation.unit__text import Unit_Text


class VariableGroup_LEGEND_PROBABILITY(SimScaleModel):
    legend: Unit_Text | None = Field(validation_alias="Legend", serialization_alias="Legend", default=None)
    probability_pct: Unit_Dimensionless | None = Field(
        validation_alias="Probability [%]", serialization_alias="Probability [%]", default=None
    )
