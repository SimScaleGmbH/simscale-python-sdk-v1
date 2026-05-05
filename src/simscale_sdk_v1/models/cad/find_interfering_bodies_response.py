from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.interference import Interference


class FindInterferingBodiesResponse(SimScaleModel):
    body_pairs: list[Interference] = Field(description="List of overlapping solid regions' pairs.")
