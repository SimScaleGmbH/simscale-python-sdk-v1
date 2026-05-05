from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.force_preload import ForcePreload
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class BoltPreloadBC(SimScaleModel):
    """Bolt preload boundary condition helps to model pre-stressed bolts in a CAD geometry for structural analysis. Enter a preload force to be assigned to cylindrical faces representing the shank of the bolt. Note:These faces should be continuous and not be assigned to contact definitions.Each bolt gets only one load, if multiple faces for the same bolt are assigned, they get ignored.The applied load does not get distributed if multiple bolts are assigned.  Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BOLT_PRELOAD",
        description="Bolt preload boundary condition helps to model pre-stressed bolts in a CAD geometry for structural analysis. Enter a preload force to be assigned to cylindrical faces representing the shank of the bolt. Note:These faces should be continuous and not be assigned to contact definitions.Each bolt gets only one load, if multiple faces for the same bolt are assigned, they get ignored.The applied load does not get distributed if multiple bolts are assigned.  Learn more.  Schema name: BoltPreloadBC",
    )
    name: str | None = Field(default=None)
    preload: ForcePreload | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
