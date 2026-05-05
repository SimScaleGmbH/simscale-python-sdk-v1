from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.friction_velocity_result_type import FrictionVelocityResultType


class FieldCalculationsFrictionVelocityResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="FRICTION_VELOCITY_U_TAU",
        description="Schema name: FieldCalculationsFrictionVelocityResultControl",
    )
    name: str | None = Field(default=None)
    result_type: FrictionVelocityResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
