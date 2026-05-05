from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FloatingPotential(SimScaleModel):
    """Specify a floating potential on a boundary or a body for conductive bodies with a constant but unspecified voltage value."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FLOATING_POTENTIAL",
        description="Specify a floating potential on a boundary or a body for conductive bodies with a constant but unspecified voltage value.  Schema name: FloatingPotential",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
