from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__length import (
    DimensionalPartialVectorFunction_Length,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FixedValueBC(SimScaleModel):
    """This is a boundary condition for the displacement vector variable. You can define prescribed values for the displacement of the assigned groups in every coordinate direction (x,y,z) or leave it unconstrained in order to let the entity move freely. Important remarks: Choose 0 as value in order to fix your selection.Do not constrain entities in directions where a load boundary condition is applied.Do not constrain entities with multiple Dirichlet boundary conditions in one direction (overconstrained).Do not constrain slave entities of Contact Constraints as they are constrained by the master in that direction (overconstrained).Learn more."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE",
        description="This is a boundary condition for the displacement vector variable. You can define prescribed values for the displacement of the assigned groups in every coordinate direction (x,y,z) or leave it unconstrained in order to let the entity move freely. Important remarks: Choose 0 as value in order to fix your selection.Do not constrain entities in directions where a load boundary condition is applied.Do not constrain entities with multiple Dirichlet boundary conditions in one direction (overconstrained).Do not constrain slave entities of Contact Constraints as they are constrained by the master in that direction (overconstrained).Learn more.  Schema name: FixedValueBC",
    )
    name: str | None = Field(default=None)
    displacement: DimensionalPartialVectorFunction_Length | None = Field(default=None)
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
