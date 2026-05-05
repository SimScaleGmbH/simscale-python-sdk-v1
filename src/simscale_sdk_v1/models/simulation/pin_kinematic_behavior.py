from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__pin_kinematic_behavior_axial_translation import (
    OneOf_PinKinematicBehaviorAxialTranslation,
)
from simscale_sdk_v1.models.simulation.one_of__pin_kinematic_behavior_rotation import OneOf_PinKinematicBehaviorRotation


class PinKinematicBehavior(SimScaleModel):
    rotation: OneOf_PinKinematicBehaviorRotation | None = Field(default=None)
    axial_translation: OneOf_PinKinematicBehaviorAxialTranslation | None = Field(
        validation_alias="axialTranslation", serialization_alias="axialTranslation", default=None
    )
