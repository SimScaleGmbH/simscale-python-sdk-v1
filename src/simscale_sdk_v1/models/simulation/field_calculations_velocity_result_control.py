from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.vorticity_result_type import VorticityResultType


class FieldCalculationsVelocityResultControl(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="VELOCITY",
        description="Schema name: FieldCalculationsVelocityResultControl",
    )
    name: str | None = Field(default=None)
    result_type: VorticityResultType | None = Field(
        validation_alias="resultType", serialization_alias="resultType", default=None
    )
