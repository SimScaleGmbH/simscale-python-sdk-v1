from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.out_of_range_color_override import OutOfRangeColorOverride
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField


class ModelSettingsOverride(SimScaleModel):
    """Partial model settings applied as an override on top of the state's own model settings. All properties are optional; only those provided are overridden."""

    scalar_field: ScalarField | None = Field(
        validation_alias="scalarField", serialization_alias="scalarField", default=None
    )
    color_legend_scaling: Literal["FULL_RANGE", "VISIBLE_ITEMS", "VISIBLE_ITEMS_WITH_INNER_VOLUME"] | None = Field(
        validation_alias="colorLegendScaling",
        serialization_alias="colorLegendScaling",
        default=None,
        description="Overrides how the color legend range is scaled for the active scalar (see ScalarSettings.colorLegendScaling): FULL_RANGE (whole dataset), VISIBLE_ITEMS (currently visible items only), or VISIBLE_ITEMS_WITH_INNER_VOLUME (visible items plus the inner volume behind visible faces).",
    )
    out_of_range_colors: OutOfRangeColorOverride | None = Field(
        validation_alias="outOfRangeColors", serialization_alias="outOfRangeColors", default=None
    )
