from __future__ import annotations

from typing import Literal

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class CellCount(SimScaleModel):
    """An interval with the estimated cell count of the generated mesh."""

    type_: Literal["CELLS"] | None = Field(validation_alias="type", serialization_alias="type", default=None)
    value: int | None = Field(default=None)
    interval_min: int | None = Field(validation_alias="intervalMin", serialization_alias="intervalMin", default=None)
    interval_max: int | None = Field(validation_alias="intervalMax", serialization_alias="intervalMax", default=None)
