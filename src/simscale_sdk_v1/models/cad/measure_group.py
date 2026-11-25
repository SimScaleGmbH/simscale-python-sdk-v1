from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.box_hint import BoxHint
from simscale_sdk_v1.models.cad.measured_value import MeasuredValue


class MeasureGroup(SimScaleModel):
    name: str = Field(description="Localization key of the section title.")
    hint_box: BoxHint | None = Field(validation_alias="hintBox", serialization_alias="hintBox", default=None)
    measured: list[MeasuredValue] = Field(description="Measure results of the section.")
