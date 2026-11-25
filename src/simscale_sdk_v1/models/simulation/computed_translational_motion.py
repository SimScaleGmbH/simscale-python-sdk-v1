from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.external_forces import ExternalForces
from simscale_sdk_v1.models.simulation.motion_axis import MotionAxis
from simscale_sdk_v1.models.simulation.one_of__computed_translational_motion_mass_definition import (
    OneOf_ComputedTranslationalMotionMassDefinition,
)


class ComputedTranslationalMotion(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="COMPUTED_TRANSLATIONAL_MOTION",
        description="Schema name: ComputedTranslationalMotion",
    )
    mass_definition: OneOf_ComputedTranslationalMotionMassDefinition | None = Field(
        validation_alias="massDefinition", serialization_alias="massDefinition", default=None
    )
    motion_axis: MotionAxis | None = Field(
        validation_alias="motionAxis", serialization_alias="motionAxis", default=None
    )
    external_forces: ExternalForces | None = Field(
        validation_alias="externalForces", serialization_alias="externalForces", default=None
    )
