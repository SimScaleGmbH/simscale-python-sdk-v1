from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class RemotePointConnectionMarc(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="REMOTE_POINT_CONNECTION",
        description="Schema name: RemotePointConnectionMarc",
    )
    name: str | None = Field(default=None)
    behavior: Literal["DEFORMABLE", "UNDEFORMABLE"] | None = Field(
        default="UNDEFORMABLE",
        description="Behavior: Create a connector between a remote point and a set of entities of the model. The remote point can then be used in a point load or point displacement condition to apply a point force/moment load or constraint to the model.Rigid (RBE2): This option creates a kinematically rigid link between the reference point and the assigned entities. It ensures the connected nodes move and rotate as a single rigid body, which is ideal for modeling stiff components like bolts or heavy mounting brackets, but it can artificially over-stiffen the assembly.Deformable (RBE3): This option distributes the loads and displacements of the reference point to the connected nodes using a weighted interpolation. It allows the connected faces to deform and expand naturally without adding artificial stiffness, making it suitable for distributing mass or applying loads to flexible structures.",
    )
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids",
        serialization_alias="geometryPrimitiveUuids",
        default=None,
        description="Create or select the point geometry primitive which should be connected to the assigned surfaces, volumes or edges via the defined connection type.",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
