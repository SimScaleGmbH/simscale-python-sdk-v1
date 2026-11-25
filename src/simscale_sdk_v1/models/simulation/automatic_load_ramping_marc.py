from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class AutomaticLoadRampingMarc(SimScaleModel):
    reference_position: Literal["BEGINNING_OF_SIMULATION", "BEGINNING_OF_LOAD_STEP"] | None = Field(
        validation_alias="referencePosition",
        serialization_alias="referencePosition",
        default="BEGINNING_OF_LOAD_STEP",
        description="Define when the reference value for the kinematic condition is computed during the simulated time: at the beginning of the simulation or at the beginning of each load step. The target value of the automatic ramping is the difference between the input value and the computed reference. For instance, activating a zero displacement with reference computed at the beginning of the load step will keep deformation at its current value. With the reference computed at the beginning of the simulation, the value ramps up once and is then held constant over the subsequent load steps. With the reference computed at the beginning of each load step, the ramping restarts from the current value in every load step.",
    )
    release_behavior: str | None = Field(
        validation_alias="releaseBehavior",
        serialization_alias="releaseBehavior",
        default="INSTANT",
        description="Define the behavior of the boundary condition when it is deactivated. This behavior is applied during the first load step where the condition passes from active to inactive. The condition can be instantly or gradually released, typically to avoid sudden changes that can result in divergence of the simulation. Additionally, for kinematic conditions, it is possible to control the release by driving the reaction force to zero, allowing the computation of residual deformations.",
    )
