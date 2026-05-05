from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.projection_type import ProjectionType


class FortyFiveViewPredefinedCameraSettings(SimScaleModel):
    setting_type: str = Field(
        validation_alias="settingType", serialization_alias="settingType", default="FORTY_FIVE_FORTY_FIVE_VIEW"
    )
    projection_type: ProjectionType = Field(validation_alias="projectionType", serialization_alias="projectionType")
    direction_specifier: Literal[
        "X_NEGATIVE_Y_NEGATIVE_Z_NEGATIVE",
        "X_NEGATIVE_Y_NEGATIVE_Z_POSITIVE",
        "X_NEGATIVE_Y_POSITIVE_Z_NEGATIVE",
        "X_NEGATIVE_Y_POSITIVE_Z_POSITIVE",
        "X_POSITIVE_Y_NEGATIVE_Z_NEGATIVE",
        "X_POSITIVE_Y_NEGATIVE_Z_POSITIVE",
        "X_POSITIVE_Y_POSITIVE_Z_NEGATIVE",
        "X_POSITIVE_Y_POSITIVE_Z_POSITIVE",
    ] = Field(validation_alias="directionSpecifier", serialization_alias="directionSpecifier")
