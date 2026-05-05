from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class SymmetryBCMarc(SimScaleModel):
    """Use this boundary condition to define a plane of symmetry for the model by constraining the displacement normal to the plane. This allows you to simulate only a portion of a symmetric structure, significantly reducing computational requirements while maintaining physical accuracy.Important remarks:The symmetry plane acts like a contact surface for all surfaces of the assigned body which are not initially in contact with the plane. If there is an initial gap with a surface, which closes during the simulation, the contact will be activated and the surface will not pass through the symmetry plane."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="SYMMETRY",
        description="Use this boundary condition to define a plane of symmetry for the model by constraining the displacement normal to the plane. This allows you to simulate only a portion of a symmetric structure, significantly reducing computational requirements while maintaining physical accuracy.Important remarks:The symmetry plane acts like a contact surface for all surfaces of the assigned body which are not initially in contact with the plane. If there is an initial gap with a surface, which closes during the simulation, the contact will be activated and the surface will not pass through the symmetry plane.  Schema name: SymmetryBCMarc",
    )
    name: str | None = Field(default=None)
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
    geometry_primitive_uuids: list[str] | None = Field(
        validation_alias="geometryPrimitiveUuids", serialization_alias="geometryPrimitiveUuids", default=None
    )
