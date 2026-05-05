from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.fixed_value_phase_fraction_bc import FixedValuePhaseFractionBC


class OutletBackFlowPFValues(SimScaleModel):
    """It specifies the phase fraction values of the back flow. If there is no back flow, the values are ignored."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="OUTLET_BACK_FLOW_PF_VALUES",
        description="It specifies the phase fraction values of the back flow. If there is no back flow, the values are ignored.  Schema name: OutletBackFlowPFValues",
    )
    back_flow_phase_fractions: list[FixedValuePhaseFractionBC] | None = Field(
        validation_alias="backFlowPhaseFractions", serialization_alias="backFlowPhaseFractions", default=None
    )
