from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_function__mass_flow_rate import DimensionalFunction_MassFlowRate


class MassFlow(SimScaleModel):
    """Defines the mass flow rate per each face of the assignment."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MASS",
        description="Defines the mass flow rate per each face of the assignment.  Schema name: MassFlow",
    )
    value: DimensionalFunction_MassFlowRate | None = Field(default=None)
