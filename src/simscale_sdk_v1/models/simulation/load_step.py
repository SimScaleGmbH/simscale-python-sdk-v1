from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.simulation.dimensional__time import Dimensional_Time


class LoadStep(SimScaleModel):
    type_: str = Field(
        validation_alias="type", serialization_alias="type", default="LOAD_STEP", description="Schema name: LoadStep"
    )
    id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    duration: Dimensional_Time | None = Field(default=None)
