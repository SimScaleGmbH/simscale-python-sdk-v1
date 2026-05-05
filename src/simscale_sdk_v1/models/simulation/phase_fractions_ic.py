from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.phase_fraction_ic import PhaseFractionIC


class PhaseFractionsIC(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="DIMENSIONLESS_PHASE_FRACTION_IC",
        description="Schema name: PhaseFractionsIC",
    )
    associated_phase_fractions: list[PhaseFractionIC] | None = Field(
        validation_alias="associatedPhaseFractions", serialization_alias="associatedPhaseFractions", default=None
    )
