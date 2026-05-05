from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.vector_field import VectorField


class VectorSettings(SimScaleModel):
    vector_field: VectorField = Field(validation_alias="vectorField", serialization_alias="vectorField")
    scale_factor: float = Field(validation_alias="scaleFactor", serialization_alias="scaleFactor", default=0.2)
    solid_color: Color | None = Field(validation_alias="solidColor", serialization_alias="solidColor", default=None)
    coloring: Literal["BY_VECTOR_FIELD", "SOLID_COLOR"] = Field(default="BY_VECTOR_FIELD")
    minimum_clamping_range: float | None = Field(
        validation_alias="minimumClampingRange",
        serialization_alias="minimumClampingRange",
        default=None,
        description="The minimum length of (non-zero) vectors will be drawn as. Must not be larger than maximumClampingRange. Default value is the minimum length of the specified vector field.",
    )
    maximum_clamping_range: float | None = Field(
        validation_alias="maximumClampingRange",
        serialization_alias="maximumClampingRange",
        default=None,
        description="The maximum length of (non-zero) vectors will be drawn as. Must not be smaller than minimumClampingRange. Default value is the maximum length of the specified vector field.",
    )
    minimum_filtering_range: float | None = Field(
        validation_alias="minimumFilteringRange",
        serialization_alias="minimumFilteringRange",
        default=None,
        description="The required minimum length of the vectors in order to be drawn. Must not be larger than maximumFilteringRange. Default value is the minimum length of the specified vector field.",
    )
    maximum_filtering_range: float | None = Field(
        validation_alias="maximumFilteringRange",
        serialization_alias="maximumFilteringRange",
        default=None,
        description="The required maximum length of the vectors in order to be drawn. Must not be smaller than minimumFilteringRange. Default value is the maximum length of the specified vector field.",
    )
