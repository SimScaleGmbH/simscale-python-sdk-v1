from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.length import Length


class FacePairs(SimScaleModel):
    target: str = Field(description="Internal name of the face.")
    tool: str = Field(description="Internal name of the face.")
    distance: Length
