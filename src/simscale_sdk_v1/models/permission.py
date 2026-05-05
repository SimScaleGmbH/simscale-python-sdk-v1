from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.permission_level import PermissionLevel
from simscale_sdk_v1.models.permission_scope import PermissionScope


class Permission(SimScaleModel):
    """Represents an entry of an access control list"""

    scope: PermissionScope
    permission: PermissionLevel
