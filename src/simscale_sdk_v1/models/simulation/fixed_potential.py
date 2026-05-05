from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__electric_potential import Dimensional_ElectricPotential
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FixedPotential(SimScaleModel):
    """Specify a constant electric potential (voltage) on a boundary or a body."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_POTENTIAL",
        description="Specify a constant electric potential (voltage) on a boundary or a body.  Schema name: FixedPotential",
    )
    name: str | None = Field(default=None)
    potential: Dimensional_ElectricPotential | None = Field(default=None)
    potential_rms: Dimensional_ElectricPotential | None = Field(
        validation_alias="potentialRMS", serialization_alias="potentialRMS", default=None
    )
    phase: Dimensional_Angle | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
