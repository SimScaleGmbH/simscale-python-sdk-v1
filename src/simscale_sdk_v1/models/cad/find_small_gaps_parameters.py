from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.cad.length import Length


class FindSmallGapsParameters(SimScaleModel):
    maximum_distance: Length
