from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fixed_value_phase_fraction_bc import FixedValuePhaseFractionBC


class InletFixedPFValues(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_FIXED_PF_VALUES",
        description="Schema name: InletFixedPFValues",
    )
    phase_fractions: list[FixedValuePhaseFractionBC] | None = Field(
        validation_alias="phaseFractions", serialization_alias="phaseFractions", default=None
    )
