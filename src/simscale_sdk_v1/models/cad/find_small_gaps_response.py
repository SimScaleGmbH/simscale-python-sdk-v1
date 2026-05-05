from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.face_pairs import FacePairs


class FindSmallGapsResponse(SimScaleModel):
    face_pairs: list[FacePairs] = Field(description="List of face pairs indicating a gap for the given tolerance.")
