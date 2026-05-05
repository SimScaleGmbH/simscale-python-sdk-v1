from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.permission import Permission


class Permissions(SimScaleModel):
    permissions: list[Permission]
