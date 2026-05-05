from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.reporting.projection_type import ProjectionType
from simscale_sdk_v1.models.reporting.vector3_d import Vector3D


class UserInputCameraSettings(SimScaleModel):
    setting_type: str = Field(validation_alias="settingType", serialization_alias="settingType", default="USER_INPUT")
    projection_type: ProjectionType = Field(validation_alias="projectionType", serialization_alias="projectionType")
    up: Vector3D
    eye: Vector3D
    center: Vector3D
    front_plane_frustum_height: float | None = Field(
        validation_alias="frontPlaneFrustumHeight",
        serialization_alias="frontPlaneFrustumHeight",
        default=None,
        description="required only for orthogonal projection type.",
    )
    field_of_view_y_degrees: float | None = Field(
        validation_alias="fieldOfViewYDegrees",
        serialization_alias="fieldOfViewYDegrees",
        default=None,
        description="The total field of view in Y direction in degrees. Required onlyf for perspective projection type.",
    )
