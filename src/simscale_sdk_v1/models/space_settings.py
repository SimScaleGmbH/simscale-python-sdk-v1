from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.sharing_control import SharingControl


class SpaceSettings(SimScaleModel):
    sharing_control: SharingControl = Field(validation_alias="sharingControl", serialization_alias="sharingControl")
