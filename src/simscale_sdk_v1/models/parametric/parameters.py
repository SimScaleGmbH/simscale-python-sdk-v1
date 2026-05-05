from __future__ import annotations

from pydantic import ConfigDict

from simscale_sdk_v1._base import SimScaleModel


class Parameters(SimScaleModel):
    model_config = ConfigDict(extra="allow")
