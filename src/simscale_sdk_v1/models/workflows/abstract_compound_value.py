from __future__ import annotations

from simscale_sdk_v1._base import SimScaleModel


class AbstractCompoundValue(SimScaleModel):
    value_model_type: str
