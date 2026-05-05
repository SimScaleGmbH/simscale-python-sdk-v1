from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.material_update_operation import MaterialUpdateOperation


class MaterialUpdateRequest(SimScaleModel):
    """Material update request schema"""

    operations: list[MaterialUpdateOperation]
