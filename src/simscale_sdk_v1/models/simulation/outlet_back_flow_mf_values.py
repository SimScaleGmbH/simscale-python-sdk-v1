from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fixed_value_mass_fraction_bc import FixedValueMassFractionBC


class OutletBackFlowMFValues(SimScaleModel):
    """It specifies the mass fraction values of the back flow. If there is no back flow, the values are ignored."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OUTLET_BACK_FLOW_MF_VALUES",
        description="It specifies the mass fraction values of the back flow. If there is no back flow, the values are ignored.  Schema name: OutletBackFlowMFValues",
    )
    back_flow_mass_fractions: list[FixedValueMassFractionBC] | None = Field(
        validation_alias="backFlowMassFractions", serialization_alias="backFlowMassFractions", default=None
    )
