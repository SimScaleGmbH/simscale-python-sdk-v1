from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__charge_density import Dimensional_ChargeDensity
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class ChargeDensity(SimScaleModel):
    """Assign a specific charge density to a body."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="CHARGE_DENSITY",
        description="Assign a specific charge density to a body.  Schema name: ChargeDensity",
    )
    name: str | None = Field(default=None)
    charge_density: Dimensional_ChargeDensity | None = Field(
        validation_alias="chargeDensity", serialization_alias="chargeDensity", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
