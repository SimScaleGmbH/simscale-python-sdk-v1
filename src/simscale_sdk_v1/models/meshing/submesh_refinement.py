from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.meshing.one_of__submesh_refinement_sizing import OneOf_SubmeshRefinementSizing
from simscale_sdk_v1.models.meshing.topological_reference import TopologicalReference


class SubmeshRefinement(SimScaleModel):
    """The refinement type local element size allows the definition of local mesh sizings on particular faces or solids. This can be used to increase the mesh efficiency by using smaller elements only where needed, for example on contact surfaces, fillets or other regions with potentially large stress gradients. The figure shows a mesh of a bolted connection with local refinements on the contact surfaces."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SUBMESH",
        description="The refinement type local element size allows the definition of local mesh sizings on particular faces or solids. This can be used to increase the mesh efficiency by using smaller elements only where needed, for example on contact surfaces, fillets or other regions with potentially large stress gradients. The figure shows a mesh of a bolted connection with local refinements on the contact surfaces.  Schema name: SubmeshRefinement",
    )
    name: str | None = Field(default="Local element size")
    sizing: OneOf_SubmeshRefinementSizing | None = Field(default=None)
    allow_quadrangles: bool | None = Field(
        validation_alias="allowQuadrangles",
        serialization_alias="allowQuadrangles",
        default=False,
        description="This parameter determines if quadrangular surface elements shall be allowed. When disabled, only triangles will be used. Meshing with triangles only is usually more robust while quadrangular elements may lead to better results. The figure shows sample meshes with quadrangular surface elements disallowed (left) and allowed (right).",
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
