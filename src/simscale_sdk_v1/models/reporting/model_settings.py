from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.opacity import Opacity
from simscale_sdk_v1.models.reporting.part import Part
from simscale_sdk_v1.models.reporting.render_mode import RenderMode
from simscale_sdk_v1.models.reporting.scalar_field import ScalarField
from simscale_sdk_v1.models.reporting.scalar_settings import ScalarSettings
from simscale_sdk_v1.models.reporting.vector_settings import VectorSettings


class ModelSettings(SimScaleModel):
    parts: list[Part] | None = Field(
        default=None, description="The parts to show or hide in the report (see hideSelectedParts)."
    )
    hide_selected_parts: bool = Field(
        validation_alias="hideSelectedParts",
        serialization_alias="hideSelectedParts",
        default=False,
        description="If set to true, the parts array indicates the hidden parts, while the rest of the model parts are visible (blacklist). On the other hand, if set to false, then the parts array indicate the visible parts while the rest of the model parts are hidden (whitelist). If the parts array is empty, then setting this value to true will hide all the model parts, while setting it to false will show all the model parts.",
    )
    show_volumes: bool | None = Field(
        validation_alias="showVolumes",
        serialization_alias="showVolumes",
        default=False,
        description="If set to false, then volumes will be hidden unless they are mentioned explicitly, i.e. when a volume is included in the parts array, and hideSelectedParts is set to false.",
    )
    scalar_field: ScalarField | None = Field(
        validation_alias="scalarField", serialization_alias="scalarField", default=None
    )
    scalar_settings: list[ScalarSettings] | None = Field(
        validation_alias="scalarSettings", serialization_alias="scalarSettings", default=None
    )
    vector_settings: list[VectorSettings] | None = Field(
        validation_alias="vectorSettings",
        serialization_alias="vectorSettings",
        default=None,
        description="The settings for the different vectors of the model.",
    )
    opacity: Opacity | None = Field(default=None)
    render_mode: RenderMode | None = Field(
        validation_alias="renderMode", serialization_alias="renderMode", default=None
    )
    solid_color: Color | None = Field(validation_alias="solidColor", serialization_alias="solidColor", default=None)
