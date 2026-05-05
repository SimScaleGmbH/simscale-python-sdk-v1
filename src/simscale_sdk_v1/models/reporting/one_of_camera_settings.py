from __future__ import annotations
from functools import partial
from typing import Annotated, Union

from pydantic import BeforeValidator

from simscale_sdk_v1._base import parse_discriminated_union
from simscale_sdk_v1.models.reporting.forty_five_view_predefined_camera_settings import (
    FortyFiveViewPredefinedCameraSettings,
)
from simscale_sdk_v1.models.reporting.top_view_predefined_camera_settings import TopViewPredefinedCameraSettings
from simscale_sdk_v1.models.reporting.user_input_camera_settings import UserInputCameraSettings

_ONE_OF_CAMERA_SETTINGS_VARIANTS: dict[str, type] = {
    "USER_INPUT": UserInputCameraSettings,
    "TOP_VIEW": TopViewPredefinedCameraSettings,
    "FORTY_FIVE_FORTY_FIVE_VIEW": FortyFiveViewPredefinedCameraSettings,
}

OneOfCameraSettings = Annotated[
    Union[UserInputCameraSettings, TopViewPredefinedCameraSettings, FortyFiveViewPredefinedCameraSettings],
    BeforeValidator(
        partial(
            parse_discriminated_union,
            disc_key="settingType",
            variants=_ONE_OF_CAMERA_SETTINGS_VARIANTS,
        )
    ),
]
