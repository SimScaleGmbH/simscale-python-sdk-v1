from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.gap import Gap


class FindGapsResponse(SimScaleModel):
    gaps: list[Gap] = Field(description="List of detected gaps in the model.")
