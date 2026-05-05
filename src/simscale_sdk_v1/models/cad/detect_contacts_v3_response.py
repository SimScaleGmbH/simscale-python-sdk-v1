from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.region_contact import RegionContact


class DetectContactsV3Response(SimScaleModel):
    region_contacts: list[RegionContact] = Field(
        validation_alias="regionContacts",
        serialization_alias="regionContacts",
        description="List of solid regions in contact with each other.",
    )
