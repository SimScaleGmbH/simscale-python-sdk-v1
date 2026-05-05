from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class MagneticFieldNormal(SimScaleModel):
    """The magnetic field is enforced to be perpendicular to the boundary."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="MAGNETIC_FIELD_NORMAL",
        description="The magnetic field is enforced to be perpendicular to the boundary.   Schema name: MagneticFieldNormal",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
