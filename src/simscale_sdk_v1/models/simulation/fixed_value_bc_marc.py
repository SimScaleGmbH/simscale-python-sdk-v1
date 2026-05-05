from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional_partial_vector_function__length import (
    DimensionalPartialVectorFunction_Length,
)
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class FixedValueBCMarc(SimScaleModel):
    """This is a boundary condition for the displacement vector variable. You can define prescribed values for the displacement of the assigned entities in every coordinate direction (x,y,z) or leave it unconstrained in order to let the entity move freely.Important remarks:Gradually ramp the displacement values via a table or formula depending on time [t], otherwise the full movement will be applied on the first iteration already and the simulation might fail to converge.Choose 0 as value in order to fix your selection in place."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FIXED_VALUE",
        description="This is a boundary condition for the displacement vector variable. You can define prescribed values for the displacement of the assigned entities in every coordinate direction (x,y,z) or leave it unconstrained in order to let the entity move freely.Important remarks:Gradually ramp the displacement values via a table or formula depending on time [t], otherwise the full movement will be applied on the first iteration already and the simulation might fail to converge.Choose 0 as value in order to fix your selection in place.  Schema name: FixedValueBCMarc",
    )
    name: str | None = Field(default=None)
    displacement: DimensionalPartialVectorFunction_Length | None = Field(default=None)
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
