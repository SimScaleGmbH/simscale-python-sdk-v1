from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.face_contact import FaceContact


class RegionContact(SimScaleModel):
    region_a: str = Field(
        validation_alias="regionA", serialization_alias="regionA", description="Internal name of the solid region."
    )
    region_b: str = Field(
        validation_alias="regionB", serialization_alias="regionB", description="Internal name of the solid region."
    )
    face_contacts: list[FaceContact] = Field(
        validation_alias="faceContacts", serialization_alias="faceContacts", description="List of faces in contact."
    )
