from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fixed_value_mass_fraction_bc import FixedValueMassFractionBC


class InletFixedMFValues(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="INLET_FIXED_MF_VALUES",
        description="Schema name: InletFixedMFValues",
    )
    mass_fractions: list[FixedValueMassFractionBC] | None = Field(
        validation_alias="massFractions", serialization_alias="massFractions", default=None
    )
