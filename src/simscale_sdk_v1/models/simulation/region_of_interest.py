from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.advanced_roi_settings import AdvancedROISettings
from simscale_sdk_v1.models.simulation.dimensional__angle import Dimensional_Angle
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.dimensional_vector2d__length import DimensionalVector2d_Length


class RegionOfInterest(SimScaleModel):
    disc_radius: Dimensional_Length | None = Field(
        validation_alias="discRadius", serialization_alias="discRadius", default=None
    )
    center_point: DimensionalVector2d_Length | None = Field(
        validation_alias="centerPoint", serialization_alias="centerPoint", default=None
    )
    ground_height: Dimensional_Length | None = Field(
        validation_alias="groundHeight", serialization_alias="groundHeight", default=None
    )
    north_angle: Dimensional_Angle | None = Field(
        validation_alias="northAngle", serialization_alias="northAngle", default=None
    )
    advanced_settings: AdvancedROISettings | None = Field(
        validation_alias="advancedSettings", serialization_alias="advancedSettings", default=None
    )
