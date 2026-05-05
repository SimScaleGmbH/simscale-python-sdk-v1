from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel


class PermissionScope(SimScaleModel):
    """Information about the user to which this permission refers"""

    username: str
