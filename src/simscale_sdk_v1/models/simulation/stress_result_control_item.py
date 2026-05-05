from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.one_of__stress_result_control_item_stress_type import (
    OneOf_StressResultControlItemStressType,
)


class StressResultControlItem(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="STRESS",
        description="Schema name: StressResultControlItem",
    )
    name: str | None = Field(default=None)
    stress_type: OneOf_StressResultControlItemStressType | None = Field(
        validation_alias="stressType", serialization_alias="stressType", default=None
    )
