from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SymmetryPlaneBC(SimScaleModel):
    """This boundary condition restrains the displacement of a face in its normal direction in order to represent a symmetry plane of the structure. Use this boundary condition to reduce the model size significantly if the geometry and the loading conditions are symmetric.Important remarks: The solver uses linear relations between all three DOFs to constrian the normal movement, thus overcontraint conditions may appear if the edges of the selected faces are constrained by other displacement boundary conditions.If the assigned faces are orthogonal to a global coordinate axes, it is recommended to directly specifiy the symmetry conditions with a Fixed value boundary condition.Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SYMMETRY_PLANE",
        description="This boundary condition restrains the displacement of a face in its normal direction in order to represent a symmetry plane of the structure. Use this boundary condition to reduce the model size significantly if the geometry and the loading conditions are symmetric.Important remarks: The solver uses linear relations between all three DOFs to constrian the normal movement, thus overcontraint conditions may appear if the edges of the selected faces are constrained by other displacement boundary conditions.If the assigned faces are orthogonal to a global coordinate axes, it is recommended to directly specifiy the symmetry conditions with a Fixed value boundary condition.Learn more.  Schema name: SymmetryPlaneBC",
    )
    name: str | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
