from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FixedSupportBC(SimScaleModel):
    """If a fixed support boundary condition is used, all degrees of freedom of the selected entities are fixed at zero. This constraint is often used to model a fixation to the ground or an undeformable part.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_SUPPORT",
        description="If a fixed support boundary condition is used, all degrees of freedom of the selected entities are fixed at zero. This constraint is often used to model a fixation to the ground or an undeformable part.Learn more.  Schema name: FixedSupportBC",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
