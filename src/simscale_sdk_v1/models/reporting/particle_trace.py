from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.one_of_visualization_style import OneOfVisualizationStyle
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.seed_settings import SeedSettings


class ParticleTrace(SimScaleModel):
    seed_settings: SeedSettings = Field(validation_alias="seedSettings", serialization_alias="seedSettings")
    visualization_style: OneOfVisualizationStyle = Field(
        validation_alias="visualizationStyle", serialization_alias="visualizationStyle"
    )
    trace_both_directions: bool = Field(
        validation_alias="traceBothDirections",
        serialization_alias="traceBothDirections",
        default=True,
        description="If set to true, the trace will be computed both forwards and backwards from the seed points.",
    )
    scalar_field: ScalarField | None = Field(
        validation_alias="scalarField", serialization_alias="scalarField", default=None
    )
    solid_color: Color | None = Field(validation_alias="solidColor", serialization_alias="solidColor", default=None)
