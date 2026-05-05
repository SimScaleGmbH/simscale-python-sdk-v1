from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__charge import Dimensional_Charge
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class TotalCharge(SimScaleModel):
    """Set the total charge of a body."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TOTAL_CHARGE",
        description="Set the total charge of a body.  Schema name: TotalCharge",
    )
    name: str | None = Field(default=None)
    total_charge: Dimensional_Charge | None = Field(
        validation_alias="totalCharge", serialization_alias="totalCharge", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
