from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class FaceContact(SimScaleModel):
    face_a: str = Field(validation_alias="faceA", serialization_alias="faceA", description="Internal name of the face.")
    face_b: str = Field(validation_alias="faceB", serialization_alias="faceB", description="Internal name of the face.")
    contact_type: Literal["PERFECT_FULL", "PERFECT_PARTIAL", "APPROXIMATE"] = Field(
        validation_alias="contactType",
        serialization_alias="contactType",
        description="Type of contact. It can be `PERFECT_FULL` when the faces' surfaces overlap perfectly within the modeller tolerance, `PERFECT_PARTIAL` when the faces' surfaces overlap partially within the modeller tolerance, or `APPROXIMATE` when the faces’ surfaces do not overlap but are sufficiently close within the modeller’s tolerance.",
    )
