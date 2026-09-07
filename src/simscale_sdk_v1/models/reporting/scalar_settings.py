from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField


class ScalarSettings(SimScaleModel):
    scalar_field: ScalarField = Field(validation_alias="scalarField", serialization_alias="scalarField")
    minimum_range: float | None = Field(
        validation_alias="minimumRange",
        serialization_alias="minimumRange",
        default=None,
        description="The minimum value for the color scheme to fill. Default is the minimum value of the scalar.",
    )
    maximum_range: float | None = Field(
        validation_alias="maximumRange",
        serialization_alias="maximumRange",
        default=None,
        description="The maximum value for the color scheme to fill. Default is the maximum value of the scalar.",
    )
    node_average_value: bool | None = Field(
        validation_alias="nodeAverageValue",
        serialization_alias="nodeAverageValue",
        default=False,
        description="Specify if the scalar result should be shown as a node averaged result or not.",
    )
    number_of_divisions: int | None = Field(
        validation_alias="numberOfDivisions",
        serialization_alias="numberOfDivisions",
        default=20,
        description="The number of divisions in the legend. If set to 0, this will create a continuous (gradient) legend with a smooth interpolation between the colors.",
    )
    color_scheme: (
        Literal[
            "NORMAL",
            "NORMAL_INVERTED",
            "BLACK_TO_WHITE",
            "WHITE_TO_BLACK",
            "GREEN_TO_BROWN",
            "WHITE_TO_BROWN",
            "METAL_CASTING",
            "BLUE_TO_WHITE_TO_RED",
            "THERMAL_1",
            "THERMAL_2",
            "THERMAL_3",
        ]
        | None
    ) = Field(
        validation_alias="colorScheme",
        serialization_alias="colorScheme",
        default="NORMAL",
        description="The color scheme to use to map scalar values on the model and legend bar.",
    )
    color_legend_scaling: Literal["FULL_RANGE", "VISIBLE_ITEMS", "VISIBLE_ITEMS_WITH_INNER_VOLUME"] | None = Field(
        validation_alias="colorLegendScaling",
        serialization_alias="colorLegendScaling",
        default="FULL_RANGE",
        description="How the color legend range is scaled when minimumRange/maximumRange are not given. FULL_RANGE uses the whole dataset (all parts, shown or hidden). VISIBLE_ITEMS scales to only the currently visible items. VISIBLE_ITEMS_WITH_INNER_VOLUME additionally folds in the inner volume behind visible faces. Ignored when minimumRange/maximumRange are provided (an explicit range always wins).",
    )
    below_range_color: Color | None = Field(
        validation_alias="belowRangeColor", serialization_alias="belowRangeColor", default=None
    )
    above_range_color: Color | None = Field(
        validation_alias="aboveRangeColor", serialization_alias="aboveRangeColor", default=None
    )
