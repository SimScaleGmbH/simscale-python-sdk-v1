from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.automatic_load_ramping_marc import AutomaticLoadRampingMarc
from simscale_sdk_v1.models.simulation.dimensional_function__pressure import DimensionalFunction_Pressure
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class PressureBCMarc(SimScaleModel):
    """This is a pressure boundary condition representing a distributed load on the selection. It is applied normal to the surface.Important remarks:If follower pressure is activated the normal direction and surface area of the faces is updated on every iteration, otherwise only in the undeformed state is used.Gradually ramp the pressure value via a table or formula depending on time [t], otherwise the full movement will be applied on the first iteration already and the simulation might fail to converge.The applied total force depends on the surface area of the selection."""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="PRESSURE",
        description="This is a pressure boundary condition representing a distributed load on the selection. It is applied normal to the surface.Important remarks:If follower pressure is activated the normal direction and surface area of the faces is updated on every iteration, otherwise only in the undeformed state is used.Gradually ramp the pressure value via a table or formula depending on time [t], otherwise the full movement will be applied on the first iteration already and the simulation might fail to converge.The applied total force depends on the surface area of the selection.  Schema name: PressureBCMarc",
    )
    name: str | None = Field(default=None)
    pressure: DimensionalFunction_Pressure | None = Field(default=None)
    is_follower_pressure: bool | None = Field(
        validation_alias="isFollowerPressure",
        serialization_alias="isFollowerPressure",
        default=True,
        description="When enabled, the direction of the pressure load is automatically updated to remain normal to the surface as it deforms and rotates throughout the analysis. This is essential for large deformation simulations where the surface orientation changes significantly.",
    )
    suppress_load_in_contact: bool | None = Field(
        validation_alias="suppressLoadInContact",
        serialization_alias="suppressLoadInContact",
        default=False,
        description="Determines if pressure remains active on elements in contact. When Off, the pressure load is applied regardless of the contact state. When On, pressure is locally deactivated for areas of the assigned face(s) currently in an active contact state. Use this setting to more realistically model the behavior of O-rings or seals under fluid pressure.",
    )
    activate_load_steps: bool | None = Field(
        validation_alias="activateLoadSteps",
        serialization_alias="activateLoadSteps",
        default=False,
        description="Turn this option on to assign this boundary condition or contact to specific load steps in your simulation. When enabled, you can control exactly when (and for how long) this condition is applied. If this option is turned off, the boundary condition or contact is considered globally active and remains applied throughout the entire simulation time.",
    )
    load_step_uuids: list[str] | None = Field(
        validation_alias="loadStepUuids", serialization_alias="loadStepUuids", default=None
    )
    automatic_load_ramping: AutomaticLoadRampingMarc | None = Field(
        validation_alias="automaticLoadRamping", serialization_alias="automaticLoadRamping", default=None
    )
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
