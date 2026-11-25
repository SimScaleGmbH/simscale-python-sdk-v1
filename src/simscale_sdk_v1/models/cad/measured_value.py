from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.arrow import Arrow
from simscale_sdk_v1.models.cad.point_pair import PointPair
from simscale_sdk_v1.models.cad.vector import Vector


class MeasuredValue(SimScaleModel):
    description: str = Field(description="Information on the result of the measurement.")
    unit: str = Field(description="Unit of measurement.")
    value: float | None = Field(default=None, description="Value of the measurement in the correct unit.")
    vector_value: Vector | None = Field(validation_alias="vectorValue", serialization_alias="vectorValue", default=None)
    hint_line: PointPair | None = Field(validation_alias="hintLine", serialization_alias="hintLine", default=None)
    hint_arrow: Arrow | None = Field(validation_alias="hintArrow", serialization_alias="hintArrow", default=None)
    hint_point: Vector | None = Field(validation_alias="hintPoint", serialization_alias="hintPoint", default=None)
