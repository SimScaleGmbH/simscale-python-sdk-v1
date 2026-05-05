from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.color import Color
from simscale_sdk_v1.models.reporting.opacity import Opacity
from simscale_sdk_v1.models.reporting.render_mode import RenderMode


class Part(SimScaleModel):
    part_identifier: str = Field(
        validation_alias="partIdentifier",
        serialization_alias="partIdentifier",
        description="The identifier of the part in the result.",
    )
    parent_identifier: str | None = Field(
        validation_alias="parentIdentifier",
        serialization_alias="parentIdentifier",
        default=None,
        description="The identifier of the parent of the part in the result. This value is necessary in cases where multiple parts appear in the result with the same name/identifier.",
    )
    opacity: Opacity | None = Field(default=None)
    render_mode: RenderMode | None = Field(
        validation_alias="renderMode", serialization_alias="renderMode", default=None
    )
    solid_color: Color | None = Field(validation_alias="solidColor", serialization_alias="solidColor", default=None)
