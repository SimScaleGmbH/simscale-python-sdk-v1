from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__force import Dimensional_Force
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.topological_reference import TopologicalReference


class BoltPreloadBCMarc(SimScaleModel):
    """Bolt preload boundary condition allows you to model pre-stressed fasteners in structural assemblies by assigning clamping conditions directly to solid volumes representing the bolt shanks. For each assigned volume, an individual bolt preload with the defined value is created and evaluated independently.Note:Ramping phase: During the first active load step, the specified force or displacement linearly ramps up from zero to your target value.Locked phase: From the second active load step onwards, the solver automatically imposes a zero axial shortening condition, locking the bolt at its current stretched length so it properly resists external loads.Open condition: If a bolt volume has no active preload boundary condition during a given load step, it enters an "open" state where it cannot resist external forces. To ensure an already tightened bolt resists external loads in subsequent stages without adding more preload, you can also specify a Length control mode with an Axial shortening of 0 m for those steps.Multiple conditions: You can apply multiple bolt preload boundary conditions to the same volume (e.g., to change tightening states across stages), provided that their active load steps do not overlap.Example: The below diagram explains the states of the bolt preload for a sample setup with four load steps, where the bolt preload is active on steps 2 and 3 and inactive on load steps 1 and 4:"""

    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="BOLT_PRELOAD",
        description='Bolt preload boundary condition allows you to model pre-stressed fasteners in structural assemblies by assigning clamping conditions directly to solid volumes representing the bolt shanks. For each assigned volume, an individual bolt preload with the defined value is created and evaluated independently.Note:Ramping phase: During the first active load step, the specified force or displacement linearly ramps up from zero to your target value.Locked phase: From the second active load step onwards, the solver automatically imposes a zero axial shortening condition, locking the bolt at its current stretched length so it properly resists external loads.Open condition: If a bolt volume has no active preload boundary condition during a given load step, it enters an "open" state where it cannot resist external forces. To ensure an already tightened bolt resists external loads in subsequent stages without adding more preload, you can also specify a Length control mode with an Axial shortening of 0 m for those steps.Multiple conditions: You can apply multiple bolt preload boundary conditions to the same volume (e.g., to change tightening states across stages), provided that their active load steps do not overlap.Example: The below diagram explains the states of the bolt preload for a sample setup with four load steps, where the bolt preload is active on steps 2 and 3 and inactive on load steps 1 and 4:  Schema name: BoltPreloadBCMarc',
    )
    name: str | None = Field(default=None)
    control_mode: Literal["LOAD", "LENGTH"] | None = Field(
        validation_alias="controlMode",
        serialization_alias="controlMode",
        default="LOAD",
        description="The Control mode determines whether the bolt pre-tensioning behavior is governed by a target force or a specific physical contraction distance. Choose Load if you know the exact clamping force required, or Length if you want to prescribe a precise adjustment displacement.",
    )
    compression_force: Dimensional_Force | None = Field(
        validation_alias="compressionForce", serialization_alias="compressionForce", default=None
    )
    axial_shortening: Dimensional_Length | None = Field(
        validation_alias="axialShortening", serialization_alias="axialShortening", default=None
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
    topological_reference: TopologicalReference | None = Field(
        validation_alias="topologicalReference", serialization_alias="topologicalReference", default=None
    )
