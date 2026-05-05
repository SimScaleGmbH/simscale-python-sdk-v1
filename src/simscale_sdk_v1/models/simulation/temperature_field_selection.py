from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class TemperatureFieldSelection(SimScaleModel):
    type_: str = Field(
        validation_alias="type",
        serialization_alias="type",
        default="TEMPERATURE",
        description="Schema name: TemperatureFieldSelection",
    )
    component_selection: Literal["TEMPERATURE"] | None = Field(
        validation_alias="componentSelection", serialization_alias="componentSelection", default="TEMPERATURE"
    )
