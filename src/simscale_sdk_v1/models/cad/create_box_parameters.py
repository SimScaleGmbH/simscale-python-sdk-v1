from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.create_box_method import CreateBoxMethod


class CreateBoxParameters(SimScaleModel):
    method: CreateBoxMethod
