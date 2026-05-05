from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SymmetryBC(SimScaleModel):
    """This boundary condition provides a symmetry condition on any face by applying a mirror effect. The fluxes and the normal components across the symmetry face are set to zero. Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SYMMETRY",
        description="This boundary condition provides a symmetry condition on any face by applying a mirror effect. The fluxes and the normal components across the symmetry face are set to zero. Learn more.  Schema name: SymmetryBC",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
