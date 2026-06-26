from __future__ import annotations

from typing import Any

from pydantic import Field

from simscale_sdk_v1._base import SimScaleModel


class UiConfiguration(SimScaleModel):
    configuration_entries: list[Any] | None = Field(
        validation_alias="configurationEntries", serialization_alias="configurationEntries", default=None
    )
