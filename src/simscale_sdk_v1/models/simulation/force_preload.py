from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__force import Dimensional_Force


class ForcePreload(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="FORCE", description="Schema name: ForcePreload"
    )
    force: Dimensional_Force | None = Field(default=None)
