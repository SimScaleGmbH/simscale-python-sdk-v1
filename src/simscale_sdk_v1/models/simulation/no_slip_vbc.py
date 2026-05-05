from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__length import Dimensional_Length
from simscale_sdk_v1.models.simulation.one_of__no_slip_vbc_no_slip_wall_roughness_type import (
    OneOf_NoSlipVBCNoSlipWallRoughnessType,
)
from simscale_sdk_v1.models.simulation.wall_contact_angle import WallContactAngle


class NoSlipVBC(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="NO_SLIP", description="Schema name: NoSlipVBC"
    )
    turbulence_wall: Literal["WALL_FUNCTION", "FULL_RESOLUTION"] | None = Field(
        validation_alias="turbulenceWall", serialization_alias="turbulenceWall", default="WALL_FUNCTION"
    )
    enable_surface_roughness: bool | None = Field(
        validation_alias="enableSurfaceRoughness",
        serialization_alias="enableSurfaceRoughness",
        default=False,
        description="When turned ON, this wall's is no longer considered to be smooth. Its roughness may be then be specified.",
    )
    surface_roughness: Dimensional_Length | None = Field(
        validation_alias="surfaceRoughness", serialization_alias="surfaceRoughness", default=None
    )
    no_slip_wall_roughness_type: OneOf_NoSlipVBCNoSlipWallRoughnessType | None = Field(
        validation_alias="noSlipWallRoughnessType", serialization_alias="noSlipWallRoughnessType", default=None
    )
    wall_contact_model: list[WallContactAngle] | None = Field(
        validation_alias="wallContactModel", serialization_alias="wallContactModel", default=None
    )
