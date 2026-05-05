from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.resource_location import ResourceLocation
from simscale_sdk_v1.models.resource_to_move import ResourceToMove


class MoveContentRequest(SimScaleModel):
    entries: list[ResourceToMove]
    to: ResourceLocation
