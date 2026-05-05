from __future__ import annotations

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel
from simscale_sdk_v1.models.space import Space


class Spaces(SimScaleModel):
    personal_spaces: list[Space] | None = Field(
        validation_alias="personalSpaces", serialization_alias="personalSpaces", default=None
    )
    team_spaces: list[Space] | None = Field(
        validation_alias="teamSpaces", serialization_alias="teamSpaces", default=None
    )
