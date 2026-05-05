from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.projection_type import ProjectionType


class TopViewPredefinedCameraSettings(SimScaleModel):
    setting_type: str = Field(validation_alias="settingType", serialization_alias="settingType", default="TOP_VIEW")
    projection_type: ProjectionType = Field(validation_alias="projectionType", serialization_alias="projectionType")
    direction_specifier: Literal["X_NEGATIVE", "X_POSITIVE", "Y_NEGATIVE", "Y_POSITIVE", "Z_NEGATIVE", "Z_POSITIVE"] = (
        Field(validation_alias="directionSpecifier", serialization_alias="directionSpecifier")
    )
