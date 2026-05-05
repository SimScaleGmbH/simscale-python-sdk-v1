from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class MagneticFluxTangential(SimScaleModel):
    """The magnetic flux is enforced to be tangential to the boundary. This boundary is often appropriate when electric current enters or leaves the boundary."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MAGNETIC_FLUX_TANGENTIAL",
        description="The magnetic flux is enforced to be tangential to the boundary. This boundary is often appropriate when electric current enters or leaves the boundary.  Schema name: MagneticFluxTangential",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
